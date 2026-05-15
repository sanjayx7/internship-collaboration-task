students = []
def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age
    }
    students.append(student)
    print("Student added successfully!\n")
def display_students():
    if not students:
        print("No students found.\n")
        return
    print("\nStudent List")
    print("-" * 30)
    for student in students:
        print(f"Roll No : {student['roll_no']}")
        print(f"Name    : {student['name']}")
        print(f"Age     : {student['age']}")
        print("-" * 30)
def search_student():
    search_roll = input("Enter Roll Number to search: ")
    for student in students:
        if student["roll_no"] == search_roll:
            print("\nStudent Found")
            print("-" * 30)
            print(f"Roll No : {student['roll_no']}")
            print(f"Name    : {student['name']}")
            print(f"Age     : {student['age']}")
            print("-" * 30)
            return
    print("Student not found.\n")
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.\n")