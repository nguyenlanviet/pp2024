import os
import gzip
import pickle
from practice_5.input import input_students, input_courses
from practice_5.domains.classes import MarkSheet
from practice_5.output import output_menu, output_courses, output_students

DATA_DIR = "data"
COMPRESSED_FILE = os.path.join(DATA_DIR, "students.pkl.gz")

def save_data(students, courses, marks_data):
    data = {'students': students, 'courses': courses, 'marks_data': marks_data}
    with gzip.open(COMPRESSED_FILE, 'wb') as compressed_file:
        pickle.dump(data, compressed_file)

def load_data():
    students = []
    courses = []
    marks_data = {}

    if os.path.exists(COMPRESSED_FILE):
        with gzip.open(COMPRESSED_FILE, 'rb') as compressed_file:
            data = pickle.load(compressed_file)
            students = data.get('students', [])
            courses = data.get('courses', [])
            marks_data = data.get('marks_data', {})

    return students, courses, marks_data

def main(stdscr):
    # ... (unchanged code)

    while True:
        stdscr.clear()
        output_menu()

        choice = stdscr.getch()
        print(f"User input: {choice}")

        if choice == ord('1'):
            output_courses(courses)
        elif choice == ord('2'):
            output_students(students)
        elif choice == ord('3'):
            mark_sheet.sort_students_by_gpa()
            save_data(students, courses, mark_sheet.marks_data)
        elif choice == ord('4'):
            print("Exiting the program.")
            break

if __name__ == "__main__":
    curses.wrapper(main)
