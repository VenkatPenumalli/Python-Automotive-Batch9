# -------------------------------
# Base Class
# -------------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_id_number(self):
        # Extract numeric part from std_001
        return int(self.student_id.split("_")[1])

    def qualify(self):
        print("Qualification rule not defined")


# -------------------------------
# Derived Class (Inheritance)
# -------------------------------
class EventParticipant(Student):

    # Polymorphism: same method, different behavior
    def qualify(self):
        if self.get_id_number() % 2 == 0:
            return "Round 1"
        else:
            return "Round 2"


# -------------------------------
# Creating 10 Student Objects
# -------------------------------
students = [
    EventParticipant("std_001", "Aarav"),
    EventParticipant("std_002", "Diya"),
    EventParticipant("std_003", "Rohan"),
    EventParticipant("std_004", "Meera"),
    EventParticipant("std_005", "Karan"),
    EventParticipant("std_006", "Ananya"),
    EventParticipant("std_007", "Vivek"),
    EventParticipant("std_008", "Pooja"),
    EventParticipant("std_009", "Arjun"),
    EventParticipant("std_010", "Neha")
]

# -------------------------------
# List 
# -------------------------------
round1_participants = []
round2_participants = []

# -------------------------------
# Qualification Process
# -------------------------------
for student in students:
    round_name = student.qualify()  # Polymorphism

    if round_name == "Round 1":
        round1_participants.append(student)
    else:
        round2_participants.append(student)

# Convert to tuple (immutable)
round1_participants = tuple(round1_participants)
round2_participants = tuple(round2_participants)

# -------------------------------
# Display Results
# -------------------------------
print("\n===== ROUND 1 PARTICIPANTS (Even IDs) =====")
for s in round1_participants:
    print(s.student_id, "-", s.name)

print("\n===== ROUND 2 PARTICIPANTS (Remaining Students) =====")
for s in round2_participants:
    print(s.student_id, "-", s.name)