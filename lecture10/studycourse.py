class StudyCourse:
    def __init__(self, name):
        self.__students = []
        self.name = name

    def add_students(self, students : list):
        self.__students.extend(students)

    def is_immatriculated(self, student_id):
        print("Private business:", self.__students)
        return student_id in self.__students

    def get_students(self):
        return self.__students

if __name__ == "__main__":
    course = StudyCourse("EGM")
    course.add_students(["sv34567", "svh1234"])
    print(course.name)
    print(course.is_immatriculated("sv34567"))
    print(course.get_students())