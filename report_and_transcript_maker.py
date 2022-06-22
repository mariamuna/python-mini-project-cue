import os.path

import student
import courses


### g. The system should be able to create a report for each student after their registration is done.These reports include
# the student’s information and information about thecourses that the student has registered this semester.

def create_report_for_a_student(student_name):
    flag = 0
    student_report_file = open("student_report.txt", "w")
    all_student_objects = student.create_student_object()
    registered_student = student.get_registered_student()
    # all_student_objects.sort(key=lambda s: s.id)

    for i in range(len(all_student_objects)):
        if all_student_objects[i].name == student_name:
            flag +=1
            if all_student_objects[i].name in registered_student:
                student_report_file.write(
                    "Student report:\n" + "    name: " + all_student_objects[i].name +
                    "\n    id: " + str(all_student_objects[i].id) + "\n    email: " + all_student_objects[i].email +
                    "\n    previous_courses: " + str(all_student_objects[i].prev_courses) +
                    "\n    previous_courses_grades_respectively: " + str(all_student_objects[i].prev_course_grades) +
                    "\n    currently_taken_courses: " + str(all_student_objects[i].current_courses) +
                    "\n    new_registered_courses: " + registered_student[all_student_objects[i].name] + "\n")
            else:
                student_report_file.write(
                    "Student report:\n" + "    name: " + all_student_objects[i].name +
                    "\n    id: " + str(all_student_objects[i].id) + "\n    email: " + all_student_objects[i].email +
                    "\n    previous_courses: " + str(all_student_objects[i].prev_courses) +
                    "\n    previous_courses_grades_respectively: " + str(all_student_objects[i].prev_course_grades) +
                    "\n    currently_taken_courses: " + str(all_student_objects[i].current_courses) +
                    "\n    new_registered_courses: null\n")

            print("the report for the student has been created\n")
            break
    if flag==0:
        student_report_file.write("this student is not registered")

    student_report_file.close()


# h. The system should be able to create a report for each course. These reports include the
# information about the course and information about the students who have registered in that course.

def get_individual_course_with_registered_students():
    if os.path.exists("new_register_courses.txt"):
        register_course_file = open("new_register_courses.txt".strip(), 'r')
        register_course_list = []
        registered_courses_with_students = {}
        for line in register_course_file:
            register_course_list.append(line.split())

        for i in range(len(register_course_list)):
            course_list = register_course_list[i][2].split(",")  ## file a registerd course gulo string from a ase segulake list a convert krsi
            registered_courses_with_students.update({register_course_list[i][0]: course_list})

        all_registered_courses = []
        for x in registered_courses_with_students:
            for j in range(len(registered_courses_with_students[x])):
                all_registered_courses.append(registered_courses_with_students[x][j])

        all_registered_course_list = list(set(all_registered_courses))
        every_course_with_students = {}
        for i in range(len(all_registered_course_list)):
            student_list = []
            for x in registered_courses_with_students:
                if all_registered_course_list[i] in registered_courses_with_students[x]:
                    student_list.append(x)
                    every_course_with_students.update({all_registered_course_list[i]: student_list})

        return every_course_with_students


def create_report_for_a_course(course_name):
    flag = 0
    course_report_file = open("course_report.txt", "w")
    all_course_objects = courses.create_course_object()
    every_course_with_assigned_students = get_individual_course_with_registered_students()
    # all_course_objects.sort(key=lambda s: s.name)

    for i in range(len(all_course_objects)):
        if all_course_objects[i].name == course_name:
            flag +=1
            if all_course_objects[i].name in every_course_with_assigned_students:
                course_report_file.write(
                    "Course report:" + "\n\n course_name: " + all_course_objects[i].name +
                    "\n time: " + all_course_objects[i].time + " days: " + all_course_objects[i].days +
                    "\n no_of_credits: " + str(all_course_objects[i].credits) +
                    "\n course_instructor: " + all_course_objects[i].instructor +
                    "\n class_location: " + all_course_objects[i].class_location +
                    "\n pre-requisite_courses: " + all_course_objects[i].pre_requisite +
                    "\n students_registered_in_this_course: " + str(
                        every_course_with_assigned_students[all_course_objects[i].name]) + "\n")
            else:
                course_report_file.write(
                    "Course report:" + "\n\n course_name: " + all_course_objects[i].name +
                    "\n time: " + all_course_objects[i].time + " days: " + all_course_objects[i].days +
                    "\n no_of_credits: " + str(all_course_objects[i].credits) +
                    "\n course_instructor: " + all_course_objects[i].instructor +
                    "\n class_location: " + all_course_objects[i].class_location +
                    "\n pre-requisite_courses: " + all_course_objects[i].pre_requisite +
                    "\n students_registered_in_this_course: no student registered in this course currently" + "\n")


            print("the report for the course has been created\n")
            break
    if flag == 0:
        course_report_file.write("course is not available!")
    course_report_file.close()



def get_transcript(student_name):
    transcript_file = open("transcripts.txt","w")
    all_student_objects = student.create_student_object()
    # all_student_objects.sort(key=lambda s: s.id)
    flag=0

    for i in range(len(all_student_objects)):
        if all_student_objects[i].name == student_name:
            flag+=1
            transcript_file.write("Transcript:\n"+"    name: " + all_student_objects[i].name +
                    "\n    id: " + str(all_student_objects[i].id) + "\n    email: " + all_student_objects[i].email+
                    "\n\nCourses        Results\n")

            for j in range(len(all_student_objects[i].prev_courses)):
                transcript_file.write(all_student_objects[i].prev_courses[j]+":             "+all_student_objects[i].prev_course_grades[j]+"\n")
            for j in range(len(all_student_objects[i].current_courses)):
                transcript_file.write(all_student_objects[i].prev_courses[j]+":             running\n")

            print("the transcript for the student has been created\n")
            break

    if flag == 0:
        transcript_file.write("this student is not registered!")

    transcript_file.close()

