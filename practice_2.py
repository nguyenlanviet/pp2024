class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class MarkSheet:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses
        self.marks_data = {}

    def input_marks(self):
        for student in self.students:
            self.marks_data[student.student_id] = {}
            for course in self.courses:
                mark = float(input(f"Enter the mark for student {student.student_id} in course {course.course_id}: "))
                self.marks_data[student.student_id][course.course_id] = mark

    def list_students(self):
        print("\nStudents:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Date of Birth: {student.dob}")
            print("Marks:")
            for course in self.marks_data[student.student_id]:
                print(f"Course {course}: {self.marks_data[student.student_id][course]}")

    def list_courses(self):
        print("\nCourses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

def input_students():
    student_data = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        id = int(input("Enter the student ID: "))
        name = input("Enter the student name: ")
        dob = input("Enter the student date of birth: ")
        student = Student(id, name, dob)
        student_data.append(student)
    return student_data

def input_courses():
    course_data = []
    n = int(input("Enter the number of courses: "))
    for i in range(n):
        id = int(input("Enter the course ID: "))
        name = input("Enter the course name: ")
        course = Course(id, name)
        course_data.append(course)
    return course_data

def main():
    students = input_students()
    courses = input_courses()
    mark_sheet = MarkSheet(students, courses)

    while True:
        print("\nOptions:")
        print("1. List courses")
        print("2. List students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            mark_sheet.list_courses()
        elif choice == '2':
            mark_sheet.list_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
