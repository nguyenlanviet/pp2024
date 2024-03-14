def input_students():
    student_data = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        student_info = []
        id = int(input("Enter the student ID: "))
        name = input("Enter the student name: ")
        dob = input("Enter the student date of birth: ")
        student_info.extend([id, name, dob])
        student_data.append(student_info)
    return student_data

def input_courses():
    course_data = []
    n = int(input("Enter the number of courses: "))
    for i in range(n):
        course_info = []
        id = int(input("Enter the course ID: "))
        name = input("Enter the course name: ")
        course_info.extend([id, name])
        course_data.append(course_info)
    return course_data

def input_marks(students, courses):
    marks_data = {}
    for student in students:
        marks_data[student[0]] = {}
        for course in courses:
            mark = float(input(f"Enter the mark for student {student[0]} in course {course[0]}: "))
            marks_data[student[0]][course[0]] = mark
    return marks_data

def list_courses(courses):
    print("\nCourses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students, marks_data):
    print("\nStudents:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")
        print("Marks:")
        for course in marks_data[student[0]]:
            print(f"Course {course}: {marks_data[student[0]][course]}")

def main():
    students = input_students()
    courses = input_courses()
    marks_data = input_marks(students, courses)

    while True:
        print("\nOptions:")
        print("1. List courses")
        print("2. List students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_courses(courses)
        elif choice == '2':
            list_students(students, marks_data)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


  