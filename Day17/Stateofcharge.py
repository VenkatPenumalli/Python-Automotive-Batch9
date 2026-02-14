import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class BatteryEKF:
    def __init__(self, Q_capacity, R0, R1, C1, dt):
        self.Q_capacity = Q_capacity  # Ah
        self.R0 = R0
        self.R1 = R1
        self.C1 = C1
        self.dt = dt
        self.x = np.array([0.8, 0.0])
        self.P = np.eye(2) * 0.01
        self.Q = np.diag([1e-6, 1e-5])  
        self.R = np.array([[0.01]])     
    def ocv(self, soc):
        return 3.0 + 1.2 * soc
    def state_transition(self, x, I):
        soc, vrc = x
        soc_next = soc - (I * self.dt) / (3600 * self.Q_capacity)
        vrc_next = vrc + self.dt * (-vrc / (self.R1 * self.C1) + I / self.C1)
        return np.array([soc_next, vrc_next])
    def measurement(self, x, I):
        soc, vrc = x
        return self.ocv(soc) - vrc - I * self.R0
    def jacobian_F(self):
        return np.array([
            [1, 0],
            [0, 1 - self.dt / (self.R1 * self.C1)]
        ])
    def jacobian_H(self):
        return np.array([[1.2, -1]])
    def predict(self, I):
        F = self.jacobian_F()
        self.x = self.state_transition(self.x, I)
        self.P = F @ self.P @ F.T + self.Q
    def update(self, V_meas, I):
        H = self.jacobian_H()
        y = V_meas - self.measurement(self.x, I)
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.x = self.x + (K.flatten() * y)
        self.P = (np.eye(2) - K @ H) @ self.P
np.random.seed(0)
n = 600
df = pd.DataFrame({
    "current": np.random.normal(5, 2, n),
    "soc_ref": np.linspace(0.8, 0.3, n)
})
df["voltage"] = 3.0 + 1.2 * df["soc_ref"] - 0.01 * df["current"] \
                + np.random.normal(0, 0.02, n)
ekf = BatteryEKF(
    Q_capacity=50,
    R0=0.01,
    R1=0.015,
    C1=2400,
    dt=1.0
)
soc_est, soc_std = [], []
for _, row in df.iterrows():
    ekf.predict(row["current"])
    ekf.update(row["voltage"], row["current"])
    soc_est.append(ekf.x[0])
    soc_std.append(np.sqrt(ekf.P[0, 0]))
df["soc_est"] = soc_est
df["soc_upper"] = df["soc_est"] + 2 * np.array(soc_std)
df["soc_lower"] = df["soc_est"] - 2 * np.array(soc_std)
rmse = np.sqrt(np.mean((df["soc_est"] - df["soc_ref"])**2))
print(f"RMSE: {rmse:.4f}")
def jacobian_check():
    ekf = BatteryEKF(50, 0.01, 0.015, 2400, 1.0)
    eps = 1e-5
    I = 5.0
    x0 = ekf.x.copy()
    f0 = ekf.state_transition(x0, I)
    J_num = np.zeros((2, 2))
    for i in range(2):
        dx = np.zeros(2)
        dx[i] = eps
        f1 = ekf.state_transition(x0 + dx, I)
        J_num[:, i] = (f1 - f0) / eps
    J_ana = ekf.jacobian_F()
    print("Jacobian error:", np.linalg.norm(J_num - J_ana))
jacobian_check()
capacity_history = [50, 49.7, 49.3, 49.0, 48.6]
soh = capacity_history[-1] / capacity_history[0]
print(f"Estimated SOH: {soh*100:.2f}%")
plt.figure(figsize=(10, 5))
plt.plot(df["soc_ref"], label="Reference SOC")
plt.plot(df["soc_est"], label="Estimated SOC")
plt.fill_between(
    df.index,
    df["soc_lower"],
    df["soc_upper"],
    alpha=0.25,
    label="Confidence Band"
)
plt.xlabel("Time Step")
plt.ylabel("SOC")
plt.title("SOC Estimation using EKF (1-RC Model)")
plt.legend()
plt.grid()
plt.show()