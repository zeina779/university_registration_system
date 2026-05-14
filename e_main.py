from b_practical_course import PracticalCourse
from c_theoritical_course import TheoreticalCourse
from d_student_schedule import StudentSchedule


# Available Courses
course1 = PracticalCourse(
    "CS101",
    "Programming Lab",
    3,
    150
)

course2 = TheoreticalCourse(
    "MATH201",
    "Discrete Mathematics",
    3,
    0.05
)

course3 = PracticalCourse(
    "PHY111",
    "Physics Lab",
    2,
    100
)

course4 = TheoreticalCourse(
    "ENG301",
    "Technical Writing",
    2,
    0.05
)

available_courses = [
    course1,
    course2,
    course3,
    course4
]

# Student Schedule
schedule = StudentSchedule()


# Main Program Loop
while True:

    print("\n===== University Registration System =====")

    print("1. View Available Courses")
    print("2. Register Course")
    print("3. View Schedule")
    print("4. Print Tuition Bill")
    print("5. Exit")

    try:

        choice = int(input("\nEnter your choice: "))

        # View Courses
        if choice == 1:

            print("\n===== Available Courses =====")

            for course in available_courses:

                course.display_course_info()

        # Register Course
        elif choice == 2:

            course_id = input("Enter Course ID: ")

            found = False

            for course in available_courses:

                if course.course_id.lower() == course_id.lower():

                    schedule.add_course(course)

                    found = True
                    break

            if not found:

                print("Course not found!")

        # View Schedule
        elif choice == 3:

            schedule.view_schedule()

        # Print Bill
        elif choice == 4:

            schedule.print_bill()

        # Exit
        elif choice == 5:

            print("Exiting system...")

            break

        else:

            print("Invalid choice! Please choose from 1 to 5.")

    except ValueError:

        print("Invalid input! Please enter a number.")