import os
import courses
import student


class Admin:
    @staticmethod
    def registration(student_name,prev_courses_and_grades, new_apply_courses):
        course_and_prerequisite = courses.get_all_courses_with_prerequisite()
        new_registered_courses = []

        if prev_courses_and_grades == -1:
            print(student_name+" is not enrolled so can not register.Please add this student in a student list first")
            return -1
        else:
            for i in range(len(new_apply_courses)):
                count = 0
                if new_apply_courses[i] in course_and_prerequisite:
                    for j in range(len(course_and_prerequisite[new_apply_courses[i]])):
                        if course_and_prerequisite[new_apply_courses[i]][j] not in prev_courses_and_grades or 2.0 >= \
                                prev_courses_and_grades[course_and_prerequisite[new_apply_courses[i]][j]] >= 4.0:
                            count += 1
                    if count > 0:
                        print(str(new_apply_courses[
                                      i]) + " can not be added because either she/he has not done or failed in the pre-requisite course ")

                    else:
                        new_registered_courses.append(new_apply_courses[i])
                        print(str(new_apply_courses[i]) + " has been registered for "+student_name)

                else:
                    print("course " + str(new_apply_courses[i]) + " is not available!")

        new_regi_courses = ''
        for i in range(len(new_registered_courses)):
            new_regi_courses += new_registered_courses[i]
            if i != len(new_registered_courses) - 1:
                new_regi_courses += ','
        return new_regi_courses

    # e. The admin should be able to register a student in all their selected courses.
    # f. The admin should be able to register all the students in a selected course at once.

    def register_all_student(self,students_with_the_course_list):
        if os.path.exists("new_register_courses.txt"):
            for x in students_with_the_course_list:
                if x in student.get_registered_student():
                    print(x+" has already been registered so can not register twice!")
                else:
                    new_registered_course_file = open("new_register_courses.txt", 'a')
                    for x in students_with_the_course_list:
                        new_registered_course = Admin.registration(x,student.get_student_previous_course_history(x),
                                                                   students_with_the_course_list[x])
                        if new_registered_course != '':
                            new_registered_course_file.write(str(x) + " has_been_registered_in_course: " + str(new_registered_course))
                            new_registered_course_file.write("\n")

        else:
            new_registered_course_file = open("new_register_courses.txt", 'a')
            for x in students_with_the_course_list:
                new_registered_course = Admin.registration(student.get_student_previous_course_history(x),
                                                           students_with_the_course_list[x])
                if new_registered_course != '':
                    new_registered_course_file.write(
                        x + " has_been_registered_in_course: " + new_registered_course)
                    new_registered_course_file.write("\n")
            new_registered_course_file.close()


def get_upcoming_register_student_with_subject_list():
    students_with_new_course_list = {}
    no_of_student_of_registration = int(input("how many students wants to register courses? "))
    for i in range(no_of_student_of_registration):
        name_of_student = input("name of student " + str(i + 1) + ": ")
        no_of_course_to_register = int(input("how many courses " + name_of_student + " wants to register?"))
        new_course_list = []
        for j in range(no_of_course_to_register):
            name_of_course = input(("whats the name of no " + str(j + 1) + " course? "))
            new_course_list.append(name_of_course)
        students_with_new_course_list.update({name_of_student: list(new_course_list)})
    return students_with_new_course_list

