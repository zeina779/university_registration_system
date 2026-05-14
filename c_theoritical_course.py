from a_course import Course

class TheoreticalCourse(Course):

    COST_PER_HOUR = 300

    def __init__(self, course_id, name, credit_hours, tech_fee):

        super().__init__(course_id, name, credit_hours)

        self.tech_fee = tech_fee

    def calculate_tuition(self):

        base = self.get_credit_hours() * self.COST_PER_HOUR

        return base + (base * self.tech_fee)

    def display_course_info(self):

        print(f"[Theoretical] {self.course_id} - {self.name}")
        print(f"Credit Hours: {self.get_credit_hours()}")
        print(f"Technology Fee: {int(self.tech_fee * 100)}%")
        print("----------------------------")