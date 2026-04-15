import json
import os

FILE = "students.json"

# Load data
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add student
def add_student():
    data = load_data()
    sid = input("Enter ID: ")

    for s in data:
        if s["id"] == sid:
            print("ID already exists!")
            return

    name = input("Enter Name: ")
    grade = input("Enter Grade: ")

    data.append({"id": sid, "name": name, "grade": grade})
    save_data(data)
    print("Student added!")

# View students
def view_students():
    data = load_data()
    if not data:
        print("No records found!")
        return

    for s in data:
        print(s)

# Delete student
def delete_student():
    data = load_data()
    sid = input("Enter ID to delete: ")

    new_data = [s for s in data if s["id"] != sid]
    save_data(new_data)
    print("Deleted successfully!")

# Menu
while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        delete_student()
    elif ch == "4":
        break
    else:
        print("Invalid choice")