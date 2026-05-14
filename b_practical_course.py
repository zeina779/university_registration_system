from a_course import Course

class PracticalCourse(Course):

    COST_PER_HOUR = 300

    def __init__(self, course_id, name, credit_hours, lab_fee):

        super().__init__(course_id, name, credit_hours)

        self.lab_fee = lab_fee

    def calculate_tuition(self):

        return (self.get_credit_hours() * self.COST_PER_HOUR) + self.lab_fee

    def display_course_info(self):

        print(f"[Practical] {self.course_id} - {self.name}")
        print(f"Credit Hours: {self.get_credit_hours()}")
        print(f"Lab Fee: ${self.lab_fee}")
        print("----------------------------")