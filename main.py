students = []


def menu():

    print("\n" + "=" * 50)
    print("STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Search Student by Roll Number")
    print("4. Update Student Marks")
    print("5. Delete Student Record")
    print("6. Exit")


def add_student():

    try:

        roll_no = int(input("Enter Roll Number: "))

        if roll_no <= 0:
            print("Roll Number must be positive!")
            return

        for student in students:
            if student["roll_no"] == roll_no:
                print("Roll Number already exists!")
                return

        name = input("Enter Student Name: ").strip()

        if name == "":
            print("Name cannot be empty!")
            return

        age = int(input("Enter Age: "))

        if age < 5 or age > 100:
            print("Age must be between 5 and 100!")
            return

        grade = input("Enter Class/Grade: ").strip()

        if grade == "":
            print("Grade cannot be empty!")
            return

        math = float(input("Enter Math Marks: "))
        physics = float(input("Enter Physics Marks: "))
        python_marks = float(input("Enter Python Marks: "))

        if (math < 0 or math > 100 or
            physics < 0 or physics > 100 or
            python_marks < 0 or python_marks > 100):

            print("Marks must be between 0 and 100!")
            return

        total = math + physics + python_marks
        percentage = (total / 300) * 100

        student = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "grade": grade,
            "marks": {
                "Math": math,
                "Physics": physics,
                "Python": python_marks
            },
            "total": total,
            "percentage": percentage
        }

        students.append(student)

        print("\nStudent Record Added Successfully!")
        print("-" * 50)

    except ValueError:
        print("Invalid Input! Please enter correct data type.")


def view_students():

    if not students:
        print("No Records Found!")
        return

    print("\n" + "-" * 90)

    print(f"{'Roll':<10}"
          f"{'Name':<15}"
          f"{'Age':<10}"
          f"{'Grade':<15}"
          f"{'Total':<10}"
          f"{'Percentage':<10}")

    print("-" * 90)

    for student in students:

        print(f"{student['roll_no']:<10}"
              f"{student['name']:<15}"
              f"{student['age']:<10}"
              f"{student['grade']:<15}"
              f"{student['total']:<10}"
              f"{student['percentage']:.2f}")

    print("-" * 90)


def search_student():

    if not students:
        print("No Records Found!")
        return

    try:

        roll = int(input("Enter Roll Number to Search: "))

        for student in students:

            if student["roll_no"] == roll:

                print("\nStudent Found!")
                print("-" * 40)

                print(f"Roll Number : {student['roll_no']}")
                print(f"Name        : {student['name']}")
                print(f"Age         : {student['age']}")
                print(f"Grade       : {student['grade']}")

                print("\nMarks:")
                print(f"Math        : {student['marks']['Math']}")
                print(f"Physics     : {student['marks']['Physics']}")
                print(f"Python      : {student['marks']['Python']}")

                print(f"\nTotal       : {student['total']}")
                print(f"Percentage  : {student['percentage']:.2f}")

                print("-" * 40)

                return

        print("Student Not Found!")

    except ValueError:
        print("Invalid Roll Number!")


def update_marks():

    if not students:
        print("No Records Found!")
        return

    try:

        roll = int(input("Enter Roll Number to Update: "))

        for student in students:

            if student["roll_no"] == roll:

                print("\nEnter New Marks")

                math = float(input("Enter Math Marks: "))
                physics = float(input("Enter Physics Marks: "))
                python_marks = float(input("Enter Python Marks: "))

                if (math < 0 or math > 100 or
                    physics < 0 or physics > 100 or
                    python_marks < 0 or python_marks > 100):

                    print("Marks must be between 0 and 100!")
                    return

                student["marks"]["Math"] = math
                student["marks"]["Physics"] = physics
                student["marks"]["Python"] = python_marks

                total = math + physics + python_marks
                percentage = (total / 300) * 100

                student["total"] = total
                student["percentage"] = percentage

                print("\nMarks Updated Successfully!")
                print("-" * 50)

                return

        print("Student Not Found!")

    except ValueError:
        print("Invalid Input!")


def delete_student():

    if not students:
        print("No Records Found!")
        return

    try:

        roll = int(input("Enter Roll Number to Delete: "))

        for student in students:

            if student["roll_no"] == roll:

                confirm = input("Are you sure you want to delete? (Y/N): ")

                if confirm.lower() == "y":

                    students.remove(student)

                    print("\nStudent Record Deleted Successfully!")
                    print("-" * 50)

                else:
                    print("Deletion Cancelled!")

                return

        print("Student Not Found!")

    except ValueError:
        print("Invalid Roll Number!")


def main():

    while True:

        menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("\nThank you for using Student Record Management System!")
            break

        else:
            print("Invalid Choice! Please enter between 1 and 6.")


main()
