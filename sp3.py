student = (101, "Alice")
op = input("Do you want to change your name? ")
if op == "yes":
    change = input("Type the new name: ")
    student = (student[0], change)
print("ID:", student[0], "Name:", student[1])