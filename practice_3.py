import math
import numpy as np
import curses

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
                mark = math.floor(mark)  # Round down to 1-digit decimal
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

    def calculate_gpa(self, student_id):
        total_credits = 0
        weighted_sum = 0

        for course in self.courses:
            credit = float(input(f"Enter the credit for course {course.course_id}: "))
            total_credits += credit
            weighted_sum += self.marks_data[student_id][course.course_id] * credit

        if total_credits == 0:
            return 0  # Avoid division by zero
        else:
            return weighted_sum / total_credits

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: self.calculate_gpa(student.student_id), reverse=True)

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

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor

    students = input_students()
    courses = input_courses()
    mark_sheet = MarkSheet(students, courses)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Options:")
        stdscr.addstr(1, 0, "1. List courses")
        stdscr.addstr(2, 0, "2. List students")
        stdscr.addstr(3, 0, "3. Calculate GPA and Sort by GPA")
        stdscr.addstr(4, 0, "4. Exit")
        stdscr.addstr(5, 0, "Enter your choice: ")

        choice = stdscr.getch()

        if choice == ord('1'):
            mark_sheet.list_courses()
        elif choice == ord('2'):
            mark_sheet.list_students()
        elif choice == ord('3'):
            mark_sheet.sort_students_by_gpa()
        elif choice == ord('4'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
