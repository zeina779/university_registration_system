class StudentSchedule:

    def __init__(self):

        self.courses = []

    def add_course(self, course):

        # منع تكرار الكورس
        for registered_course in self.courses:

            if registered_course.course_id == course.course_id:

                print("Course already registered!")
                return

        self.courses.append(course)

        print(f"{course.name} added successfully!")

    def view_schedule(self):

        if not self.courses:

            print("No courses registered yet.")
            return

        print("\n===== Student Schedule =====")

        for course in self.courses:

            print(f"{course.course_id} - {course.name}")

    def print_bill(self):

        if not self.courses:

            print("No courses registered.")
            return

        total = 0

        print("\n========== Tuition Bill ==========")

        for course in self.courses:

            fee = course.calculate_tuition()

            print(f"{course.name}: ${fee}")

            total += fee

        print("----------------------------------")
        print(f"Total Tuition Fees: ${total}")
        print("==================================")