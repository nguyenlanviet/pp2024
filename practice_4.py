# main.py
import curses
from practice_3.input import input_students, input_courses
from practice_3.domains.classes import MarkSheet
from practice_3.output import output_menu, output_courses, output_students

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor

    students = input_students()
    courses = input_courses()
    mark_sheet = MarkSheet(students, courses)

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
        elif choice == ord('4'):
            print("Exiting the program.")
            break

if __name__ == "__main__":
    curses.wrapper(main)
