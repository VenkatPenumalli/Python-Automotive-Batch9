import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

DEADLINES = {
    "Brake_Pedal_Read": 5,   
    "ABS_Control": 10,       
    "Brake_Output": 5        
}
LOG_FILE = r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Capstone\ecu_logs.csv"

def simulate_ecu_logs(samples=50, high_load=True):

    tasks = list(DEADLINES.keys())
    system_clock = 0.0

    with open(LOG_FILE, "w") as file:
        for _ in range(samples):
            for task in tasks:
                start_time = system_clock
                base_exec = DEADLINES[task] * 0.8

                if high_load:
                    jitter = random.uniform(0, DEADLINES[task] * 0.6)
                else:
                    jitter = random.uniform(0, DEADLINES[task] * 0.3)

                execution_time = base_exec + jitter
                end_time = start_time + execution_time

                file.write(
                    f"{task},{start_time:.3f},{end_time:.3f}\n"
                )

                system_clock = end_time + random.uniform(0.5, 2)

    print("ECU Log Generated Successfully.\n")

def load_log():
    df = pd.read_csv(LOG_FILE, names=["Task", "Start", "End"])
    return df

def calculate_execution_time(df):
    df["Execution_Time_ms"] = df["End"] - df["Start"]
    return df

def analyze_performance(df):
    df["Deadline_ms"] = df["Task"].map(DEADLINES)
    df["Deviation_ms"] = df["Execution_Time_ms"] - df["Deadline_ms"]
    df["Violation"] = df["Deviation_ms"] > 0
    return df

def calculate_statistics(df):
    result = []
    for task in df["Task"].unique():
        task_df = df[df["Task"] == task]
        wcet = task_df["Execution_Time_ms"].max()
        bcet = task_df["Execution_Time_ms"].min()
        avg = task_df["Execution_Time_ms"].mean()
        jitter = wcet - bcet
        violations = task_df["Violation"].sum()
        result.append([
            task,
            round(wcet, 3),
            round(bcet, 3),
            round(avg, 3),
            round(jitter, 3),
            violations
        ])

    stats_df = pd.DataFrame(result, columns=[
        "Task", "WCET(ms)", "BCET(ms)",
        "Average(ms)", "Jitter(ms)", "Violations"
    ])
    return stats_df

def generate_graph(df):
    for task in df["Task"].unique():
        task_df = df[df["Task"] == task]
        plt.figure()
        plt.plot(task_df["Execution_Time_ms"])
        plt.title(f"{task} Execution Time")
        plt.xlabel("Samples")
        plt.ylabel("Execution Time (ms)")
        plt.axhline(DEADLINES[task])
        plt.show()
        
def main():
    print("Simulating ECU Logs...\n")
    simulate_ecu_logs(samples=50, high_load=True)

    print("Loading Logs...")
    df = load_log()

    print("Calculating Execution Time...")
    df = calculate_execution_time(df)

    print("Analyzing Performance...")
    df = analyze_performance(df)

    print("\nDetailed Performance Data:\n")
    print(df.head())

    print("\nCalculating Statistics...\n")
    stats_df = calculate_statistics(df)

    print("===== PERFORMANCE SUMMARY =====")
    print(stats_df)

    # Export CSV report
    df.to_csv("detailed_performance.csv", index=False)
    stats_df.to_csv("summary_report.csv", index=False)

    print("\nCSV Reports Generated.")

    print("\nGenerating Graphs...")
    generate_graph(df)

if __name__ == "__main__":
    main()    