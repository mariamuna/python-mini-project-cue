### c. The list of students is given in a text file with the following format:
# a. Student name, Student ID, Student email address, [List of previous courses separated by comma],
# [List of the grades in those courses separated by comma], [List of courses currently registered separated by comma]
# b. The students are separated by newline.

### d. A student can register in a course if and only if they passed the required prerequisite.
import os
from curses.ascii import isdigit

import courses
class Student:

    def __init__(self, name, id, email, prev_courses, prev_course_grades, current_courses):
        self.name = name
        self.id = id
        self.email = email
        self.prev_courses = prev_courses
        self.prev_course_grades = prev_course_grades
        self.current_courses = current_courses

def create_student_file():
    student_file = open("student.txt", "a")

    no_of_total_students = int(input("how many students? "))
    student_list = []
    for i in range(no_of_total_students):
        student_name = input("write the name of the student " + str(i + 1) + ": ")
        student_list.append(student_name)

    for i in range(len(student_list)):
        print("Student " + str(i + 1) + ": ")
        full_name = input("write the full name using underscore of " + str(student_list[i]))
        id = input("write the id of " + str(student_list[i]) + ": ")
        email = input("write the email of " + str(student_list[i]) + ": ")
        no_of_prev_courses = int(input("how many previous courses of " + str(student_list[i]) + ": "))
        prev_courses = ''
        prev_course_grades = ''
        if no_of_prev_courses == 0:
            prev_courses += 'null'
            prev_course_grades += 'null'
        else:
            for j in range(no_of_prev_courses):
                prev_course_name = input("previous course " + str(j + 1) + " of " + str(student_list[i]) + ": ")
                prev_course_grade = float(
                    input("grade of course " + prev_course_name + " of " + str(student_list[i]) + ": "))
                prev_courses += prev_course_name
                if j != no_of_prev_courses - 1:
                    prev_courses += ','
                prev_course_grades += str(prev_course_grade)
                if j != no_of_prev_courses - 1:
                    prev_course_grades += ','

        no_of_current_course = int(input("how many courses " + str(student_list[i]) + " doing currently? "))
        current_courses = ''
        if no_of_current_course == 0:
            current_courses+= "null"
        if no_of_prev_courses == 0:
            prev_courses += 'null'
            prev_course_grades += 'null'
        else:
            for j in range(no_of_current_course):
                current_course_name = input("current course " + str(j + 1) + " of " + str(student_list[i]) + ": ")
                current_courses += current_course_name
                if j != no_of_current_course - 1:
                    current_courses += ','

        filesize = os.path.getsize("student.txt")
        if filesize == 0:
            student_file.write("Student: " + str(i + 1) + " name: " + full_name + " id: " + id +
                               " email: " + email + " previous_courses: " + str(prev_courses) +
                               " previous_courses_grades_respectively: " + str(prev_course_grades) +
                               " currently_taken_courses: " + str(current_courses) + "\n")
        else:
            x = len(open("student.txt", "r").readlines())
            student_file.write("Student: " + str(i + 1 + x) + " name: " + full_name + " id: " + id +
                               " email: " + email + " previous_courses: " + str(prev_courses) +
                               " previous_courses_grades_respectively: " + str(prev_course_grades) +
                               " currently_running_courses: " + str(current_courses) + "\n")

    student_file.close()

def get_student_details():
    student_details = []
    student_file = open("student.txt".strip(), 'r')
    for line in student_file:
        line_list = line.split()
        student_details.append(line_list)
    student_file.close()
    return student_details

def create_student_object():
    all_student_objects = []
    all_students = get_student_details()
    student_list = []
    for i in range(len(all_students)):
        student_list.append(all_students[i][1])
    for i in range(len(all_students)):
        prev_course = all_students[i][9].split(",")
        prev_course_grades = all_students[i][11].split(",")
        current_courses = all_students[i][13].split(",")
        student_list[i] = Student(all_students[i][3], int(all_students[i][5]), all_students[i][7], prev_course,
                                  prev_course_grades, current_courses)
        all_student_objects.append(student_list[i])

    return all_student_objects


def get_student_previous_course_history(student_name):
    individual_course_history = {}

    count = -1
    for i in range(len(get_student_details())):
        if student_name in get_student_details()[i]:
            count = i
            break
    if count == -1:
        return count
    else:
        course = get_student_details()[count][9].split(",")
        grade = get_student_details()[count][11].split(",")

        for i in range(len(course)):
            individual_course_history.update({course[i]: float(grade[i])})

        return individual_course_history


def get_registered_student():
    new_register_course_file = open("new_register_courses.txt".strip(), 'r')
    student_with_registered_course_list = []
    student_with_registered_courses = {}
    for line in new_register_course_file:
        list_line = line.split()
        student_with_registered_course_list.append(list_line)

    for i in range(len(student_with_registered_course_list)):
        student_with_registered_courses.update({student_with_registered_course_list[i][0]: student_with_registered_course_list[i][2]})
    new_register_course_file.close()
    return student_with_registered_courses

