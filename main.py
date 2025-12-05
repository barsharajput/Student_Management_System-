import os

FILE = "students.txt"


def add_student():
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()

    with open(FILE, "a") as f:
        f.write(f"{roll},{name},{age},{course}\n")

    print("✅ Student added successfully!")


def view_students():
    if not os.path.exists(FILE):
        print("No student records found!")
        return

    print("\n---- ALL STUDENTS ----")
    with open(FILE, "r") as f:
        for line in f:
            roll, name, age, course = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Age: {age} | Course: {course}")


def search_student():
    roll_search = input("Enter Roll Number to search: ").strip()

    if not os.path.exists(FILE):
        print("No student records found!")
        return

    with open(FILE, "r") as f:
        for line in f:
            roll, name, age, course = line.strip().split(",")
            if roll == roll_search:
                print("\n--- STUDENT FOUND ---")
                print(f"Roll: {roll}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Course: {course}")
                return

    print("❌ Student not found!")


def delete_student():
    roll_delete = input("Enter Roll Number to delete: ").strip()

    if not os.path.exists(FILE):
        print("No student records found!")
        return

    lines = []
    deleted = False

    with open(FILE, "r") as f:
        for line in f:
            roll, name, age, course = line.strip().split(",")
            if roll != roll_delete:
                lines.append(line)
            else:
                deleted = True

    with open(FILE, "w") as f:
        f.writelines(lines)

    if deleted:
        print("🗑️ Student deleted successfully!")
    else:
        print("❌ Student not found!")


def menu():
    while True:
        print("\n==== STUDENT MANAGEMENT SYSTEM ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    menu()
