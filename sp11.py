# -----------------------
# CLUB DATA (sets of tuples)
# -----------------------

coding_club = {
    (101, "Diallo", "Moussa"),
    (102, "Nakamura", "Yuki"),
    (103, "Smith", "Emma"),
    (104, "Kone", "Aminata")
}

robotics_club = {
    (102, "Nakamura", "Yuki"),
    (103, "Smith", "Emma"),
    (105, "Brown", "Lucas"),
    (106, "Okafor", "Chinedu")
}

chess_club = {
    (101, "Diallo", "Moussa"),
    (105, "Brown", "Lucas"),
    (107, "Petrov", "Ivan"),
    (108, "Rossi", "Giulia")
}

all_students = coding_club | robotics_club | chess_club

print("\n--- ALL STUDENTS ---")
for student in all_students:
    print(student)

coding_and_robotics = coding_club & robotics_club

print("\n--- CODING & ROBOTICS ---")
for student in coding_and_robotics:
    print(student)

coding_only = coding_club - robotics_club - chess_club

print("\n--- CODING ONLY ---")
for student in coding_only:
    print(student)

only_one_club = (
    (coding_club - robotics_club - chess_club) |
    (robotics_club - coding_club - chess_club) |
    (chess_club - coding_club - robotics_club)
)

print("\n--- EXACTLY ONE CLUB ---")
for student in only_one_club:
    print(student)