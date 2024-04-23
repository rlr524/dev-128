from student import Student


def show_students(students):
    print("STUDENTS")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student.first_name} {student.last_name}")
    print()


def show_student(student):
    # Set a standard column width
    w = 18
    print("STUDENT DATA")
    print(f"{'First Name':{w}} {student.first_name}")
    print(f"{'Last Name':{w}} {student.last_name}")
    print(f"{'Level':{w}} {student.level}")
    print(f"{'Age':{w}} {student.age}")
    print(f"{'Units':{w}} {student.units}")
    print(f"{'GPA':{w}} {student.get_grade_point_average():.2f}")
    print()


def get_students():
    # Return a tuple of Student objects
    return (
        Student("Madison", "Hong", "Freshman", 18, 16, 59),
        Student("Olivia", "Rodriguez", "Freshman", 18, 13, 36),
        Student("Jason", "Kim", "Sophomore", 19, 12, 47),
        Student("Jessica", "Cheng", "Freshman", 18, 16, 64),
        Student("Nicole", "Landry", "Freshman", 18, 11, 47)
    )


def get_student(students):
    while True:
        try:
            number = int(input("Enter student number: "))
            if number < 1 or number > len(students):
                print("Student number does not exist. Please try again.")
            else:
                return students[number - 1]
        except ValueError:
            print("Invalid student number. Please try again.")
        print()


def main():
    print("The student GPA viewer program")
    print()

    students = get_students()
    show_students(students)

    choice = "y"
    while choice.lower() == "y":
        student = get_student(students)
        show_student(student)

        choice = input("View another student? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
