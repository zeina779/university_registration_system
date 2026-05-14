from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, course_id, name, credit_hours):

        self.course_id = course_id
        self.name = name
        self.__credit_hours = credit_hours

    # Getter
    def get_credit_hours(self):

        return self.__credit_hours

    # Setter
    def set_credit_hours(self, hours):

        if hours > 0:

            self.__credit_hours = hours

        else:

            print("Invalid credit hours!")

    @abstractmethod
    def calculate_tuition(self):
        pass

    @abstractmethod
    def display_course_info(self):
        pass