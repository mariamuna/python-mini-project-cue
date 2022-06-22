### b. The list of available courses is given in a text file with the following format:
# a. Course number, Name of the course, Course time and days, Number of credits, Course instructor,
# Class location, Course pre-requisite b. The courses are separated by newline
import os
from collections import namedtuple
from curses.ascii import isdigit


class Course:
    def __init__(self,name,time,days,credits,instructor,class_location,pre_requisites):
        self.name = name
        self.time = time
        self.days = days
        self.credits = credits
        self.instructor = instructor
        self.class_location = class_location
        self.pre_requisite = pre_requisites

def create_course_file():
    no_of_available_courses = int(input("how many courses are available?"))
    # if no_of_available_courses != isdigit:
    #     raise ValueError("no of available courses should be an integer number!")
    courses_file = open("courses_list.txt", "a")

    for i in range(no_of_available_courses):
        course_name = input("what's the name of the course? ")
        course_time = input("Time of course " + course_name + ": ")
        course_days = input("Days of course " + course_name + ": ")
        no_of_credits = int(input("no of credit of course " + course_name + ": "))
        course_instructor = input("what's the name of the course instructor of " + course_name + ": ")
        class_location = input("write the room no of the course " + course_name + ": ")
        no_of_prerequisite_courses = int(input("how many pre-requisite courses for " + course_name + ": "))
        ## enter 0 if there is no pre requisite course

        pre_requisite_courses = ''
        if no_of_prerequisite_courses == 0:
            pre_requisite_courses += 'null'

        for j in range(no_of_prerequisite_courses):
            name_of_pre_requisite_course = input("write the name of number " + str(j + 1) + " pre requisite course: ")
            pre_requisite_courses += name_of_pre_requisite_course
            if j != no_of_prerequisite_courses - 1:
                pre_requisite_courses += ','
        filesize = os.path.getsize("courses_list.txt")
        if filesize == 0:
            courses_file.write(
                "course_number: " + str(i + 1) + " course_name: " + course_name + " course_time: " + course_time +
                " course_days: " + course_days + " no_of_credits: " + str(no_of_credits) + " course_instructor: "
                + course_instructor + " class_location: " + class_location + " pre-requisite_course: " +
                str(pre_requisite_courses) + "\n")
        else:
            x = len(open("courses_list.txt","r").readlines())
            courses_file.write(
                "course_number: " + str(i + 1 + x) + " course_name: " + course_name + " course_time: " + course_time +
                " course_days: " + course_days + " no_of_credits: " + str(no_of_credits) + " course_instructor: "
                + course_instructor + " class_location: " + class_location + " pre-requisite_course: " +
                str(pre_requisite_courses) + "\n")

    courses_file.close()

def get_course_details():
    course_details = []
    course_file = open("courses_list.txt".strip(), 'r')
    for line in course_file:
        line_list = line.split()
        course_details.append(line_list)
    course_file.close()
    return course_details

def create_course_object():
    all_course_objects = []
    all_courses = get_course_details()
    course_list = []
    for i in range(len(all_courses)):
        course_list.append(all_courses[i][1])
    for i in range(len(all_courses)):
        pre_requisites = all_courses[i][15]
        course_list[i] = Course(all_courses[i][3], all_courses[i][5], all_courses[i][7],
                        int(all_courses[i][9]),all_courses[i][11],all_courses[i][13], pre_requisites)
        all_course_objects.append(course_list[i])
    return all_course_objects


def get_all_courses_with_prerequisite():
    available_courses_with_prerequisite = {}
    courses_file = open("courses_list.txt".strip(),"r")
    course_details_list = []
    for line in courses_file:
        line_list = line.split()
        course_details_list.append(line_list)
    courses_file.close()
    for i in range(len(course_details_list)):
        pre_requisite_list = course_details_list[i][15].split(",")
        available_courses_with_prerequisite.update({course_details_list[i][3]:pre_requisite_list})
    return available_courses_with_prerequisite




