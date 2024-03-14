import curses
import os
import gzip
import pickle
from practice_4.input import input_students, input_courses
from practice_4.domains.classes import MarkSheet
from practice_4.output import output_menu, output_courses, output_students

DATA_DIR = "data"
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")
COURSES_FILE = os.path.join(DATA_DIR, "courses.txt")
MARKS_FILE = os.path.join(DATA_DIR, "marks.txt")
COMPRESSED_FILE = os.path.join(DATA_DIR, "students.dat")

def save_data(students, courses, marks_data):
    # Save student data
    with open(STUDENTS_FILE, "w") as file:
        for student in students:
            file.write(f"{student.student_id},{student.name},{student.dob}\n")

    # Save course data
    with open(COURSES_FILE, "w") as file:
        for course in courses:
            file.write(f"{course.course_id},{course.name}\n")

    # Save marks data
    with open(MARKS_FILE, "w") as file:
        for student_id, marks in marks_data.items():
            for course_id, mark in marks.items():
                file.write(f"{student_id},{course_id},{mark}\n")

def load_data():
    students = []
    courses = []
    marks_data = {}

    # Load student data
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as file:
            for line in file:
                student_id, name, dob = line.strip().split(',')
                students.append(Student(int(student_id), name, dob))

    # Load course data
    if os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, "r") as file:
            for line in file:
                course_id, name = line.strip().split(',')
                courses.append(Course(int(course_id), name))

    # Load marks data
    if os.path.exists(MARKS_FILE):
        with open(MARKS_FILE, "r") as file:
            for line in file:
                student_id, course_id, mark = line.strip().split(',')
                if student_id not in marks_data:
                    marks_data[student_id] = {}
                marks_data[student_id][course_id] = float(mark)

    return students, courses, marks_data

def compress_data():
    with open(STUDENTS_FILE, 'rb') as students_file, \
            open(COURSES_FILE, 'rb') as courses_file, \
            open(MARKS_FILE, 'rb') as marks_file, \
            gzip.open(COMPRESSED_FILE, 'wb') as compressed_file:
        compressed_data = {
            'students': students_file.read(),
            'courses': courses_file.read(),
            'marks': marks_file.read()
        }
        pickle.dump(compressed_data, compressed_file)

def decompress_data():
    with gzip.open(COMPRESSED_FILE, 'rb') as compressed_file:
        compressed_data = pickle.load(compressed_file)
        with open(STUDENTS_FILE, 'wb') as students_file, \
                open(COURSES_FILE, 'wb') as courses_file, \
                open(MARKS_FILE, 'wb') as marks_file:
            students_file.write(compressed_data['students'])
            courses_file.write(compressed_data['courses'])
            marks_file.write(compressed_data['marks'])

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor

    if os.path.exists(COMPRESSED_FILE):
        decompress_data()
        students, courses, marks_data = load_data()
    else:
        students = input_students()
        courses = input_courses()
        mark_sheet = MarkSheet(students, courses)
        mark_sheet.input_marks()
        save_data(students, courses, mark_sheet.marks_data)
        compress_data()

    while True:
        stdscr.clear()
        output_menu()

        choice = stdscr.getch()
        print(f"User input: {choice}")  # Add this line to print the user input

        if choice == ord('1'):
            output_courses(courses)
        elif choice == ord('2'):
            output_students(students)
        elif choice == ord('3'):
            mark_sheet.sort_students_by_gpa()
            save_data(students, courses, mark_sheet.marks_data)
            compress_data()
        elif choice == ord('4'):
            print("Exiting the program.")
            break
