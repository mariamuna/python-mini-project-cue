import report_and_transcript_maker
import student

# courses_done = {'a':2.5,'b':3}
# all_course_with_pre = {'d':{1:'a',2:'b'}}
# all_course_with_pre = {'d':['a','b']}
# count =0
# no_of_courses_student_want_to_register = int(input("how many courses a student want to register? "))
# for i in range(no_of_courses_student_want_to_register):
#     course_name = input("what is the no "+str(i+1)+" course name: ")
#     if course_name in all_course_with_pre:
#         for x in all_course_with_pre[course_name]:
#             if x not in courses_done or 2.0 >= courses_done[x] >= 4.0:
#                 count += 1
#                 break
#         if count>0:
#             print("sorry")
#         else:
#             print("course added")
#
#                 # print('prerequisite course has not done yet
#     else:
#         print("course is not available")

# d = {'a':1,'b':2}
# if 'c' in d:
#     print("yes")
# else:
#     print("no")
# l = [['mm',1],['nn',2],['kk',3]]
# print(l[0][0]=="mm")
# count = 0
# for i in range(len(l)):
#     if "nn" in l[i]:
#         count = i
#         break
#
# if count == 0:
#     print("no")
# else:
#     print("yes")
# done = {"a":3.0,"e":3.5,"c":4}
# course = {"d":["a","b"]}
# new_apply_courses = ["d"]

# def registration(done, new_apply_courses):
#     new_registered_courses = []
#     for i in range(len(new_apply_courses)):
#         count = 0
#         if new_apply_courses[i] in course:
#             for j in range(len(course[new_apply_courses[i]])):
#                 if course[new_apply_courses[i]][j] not in done or 2.0 >= done[course[new_apply_courses[i]][j]] >= 4.0:
#                     count += 1
#             if count > 0:
#                 print(str(new_apply_courses[
#                               i]) + " can not be added because either she/he has not done or failed in the pre-requisite course ")
#             else:
#
#                 new_registered_courses.append(new_apply_courses[i])
#                 print(str(new_apply_courses[i]) + " has been added")
#
#         else:
#             print(str(new_apply_courses[i]) + " is not available!")
# registration(done,new_apply_courses)
# from student import get_student_details
# from student import create_student_object
#

# class Student:
#
#
#     def __init__(self, name, id, email, prev_courses, prev_course_grades, current_courses):
#         self.name = name
#         self.id = id
#         self.email = email
#         self.prev_courses_and_grades = prev_courses
#         self.prev_course_grades = prev_course_grades
#         self.current_courses = current_courses
# def a():
#     no_of_total_students = int(input("how many students? "))
#     student_list = []
#     for i in range(no_of_total_students):
#         student_name = input("write the name of the student " + str(i + 1) + ": ")
#         student_list.append(student_name)
#     return student_list

# def b():
#     all_student_objects = []
#     all_student = student.get_student_details()
#     student_list = []
#     for i in range(len(all_student)):
#         student_list.append(all_student[i][1])
#     for i in range(len(all_student)):
#         prev_course = all_student[i][9].split(",")
#         prev_course_grades = all_student[i][11].split(",")
#         current_courses = all_student[i][13].split(",")
#         student_list[i] = Student(all_student[i][3], int(all_student[i][5]), all_student[i][7], prev_course,prev_course_grades, current_courses)
#         all_student_objects.append(student_list[i])
#     # all_student_objects.sort(key=lambda s: s.id)
#     # for i in range(len(all_student_objects)):
#     #     print(str(all_student_objects[i].id)+" "+all_student_objects[i].name)
#     # registered_student = student.get_registered_student()
#
#     print(student.create_student_object())

# b()

# def registration():
#     course_and_prerequisite = {"a":["a0","a1"],"b":["b0","b1"],"c":["c0","c1"]}
#     prev_courses_and_grades = {"a0":3.0,"a1":3.5,"b0":4.0,"b1":3.6,"c0":3.0}
#     new_apply_courses = ["a","b","c"]
#     new_regi_course_list = []
#     for i in range(len(new_apply_courses)):
#         count = 0
#         if new_apply_courses[i] in course_and_prerequisite:
#             for j in range(len(course_and_prerequisite[new_apply_courses[i]])):
#                 if course_and_prerequisite[new_apply_courses[i]][j] not in prev_courses_and_grades or 2.0 >= \
#                         prev_courses_and_grades[course_and_prerequisite[new_apply_courses[i]][j]] >= 4.0:
#                     count += 1
#             if count > 0:
#                 print(str(new_apply_courses[i]) + " can not be added because either she/he has not done or failed in the pre-requisite course ")
#
#             else:
#                 new_regi_course_list.append(new_apply_courses[i])
#                 print(str(new_apply_courses[i]) + " has been added")
#
#         else:
#             print("course " + str(new_apply_courses[i]) + " is not available!")
#
#     new_regi_courses = ''
#     for i in range(len(new_regi_course_list)):
#         new_regi_courses += new_regi_course_list[i]
#         if i != len(new_regi_course_list)-1:
#             new_regi_courses += ','
#     return new_regi_courses
#
#
# print(registration())
# def d():
#     print(report_and_transcript_maker.get_course_with_registered_students())
# d()


# from tkinter import *
#
# root = Tk()
# mylabel = Label(root, text="Menu")
# mylabel.pack()
#
#
# def myclick():
#     mylabel = Label(root, text="you clicked a button1")
#     mylabel.pack()
#
#
# Button(root, text="button1", padx=50, command=myclick).pack()
# e = Entry(root,width=50)
# e.pack()
# e.get()
# Button(root, text="button2", padx=50, command=myclick).pack()
# Button(root, text="button3", padx=50, command=myclick).pack()
# Button(root, text="button4", padx=50, command=myclick).pack()
# Button(root, text="button4", padx=50, command=myclick).pack()
# Button(root, text="button4", padx=50, command=myclick).pack()
# Button(root, text="button4", padx=50, command=myclick).pack()
#
# root.mainloop()

from tkinter import *
import admin
import courses
import student
from admin import Admin
import report_and_transcript_maker
from tkinter import filedialog


# def main():
#     root = Tk()
#     root.title("Menu")
#     frame = LabelFrame(root,padx=50,pady=50)
#     frame.pack(padx=50,pady=50)
#     try:
#         def myclick1():
#             courses.create_course_file()
#
#         Label(frame, text="click 1 to add courses").grid(row=0, column=0)
#         Button(frame, text="button1", padx=50, command=myclick1).grid(row=0, column=1)
#
#         def myclick2():
#             student.create_student_file()
#
#         Label(frame, text="click 2 to add courses").grid(row=1, column=0)
#         Button(frame, text="button2", padx=50, command=myclick2).grid(row=1, column=1)
#
#         def myclick3():
#             admin1 = Admin()
#             admin1.register_all_student(admin.get_upcoming_register_student_with_subject_list())
#
#         Label(frame, text="            click 3 to register all students").grid(row=2, column=0)
#         Button(frame, text="button3", padx=50, command=myclick3).grid(row=2, column=1)
#
#         def myclick4():
#             root_student_name = Tk()
#             root_student_name.title("Get a report")
#             frame = LabelFrame(root_student_name,padx=20,pady=20)
#             frame.pack(padx=20,pady=20)
#             Label(frame, text="enter the name of the student").grid(row=0,column=0)
#             e = Entry(frame, width=50)
#             e.grid(row=1,column=0)
#
#             def inner_click():
#                 report_and_transcript_maker.create_report_for_a_student(e.get())
#                 show_report = Tk()
#                 show_report.title("Report of the given student")
#                 frame = LabelFrame(show_report,padx=10,pady=10)
#                 frame.pack(padx=10,pady=10)
#                 student_file = open("student_report.txt", "r")
#                 Label(frame, text=student_file.read()).grid(row=0,column=0)
#                 student_file.close()
#                 show_report.mainloop()
#
#             Button(frame, text="enter", command=inner_click).grid(row=2,column=0)
#             Button(frame, text="go back", command=root_student_name.destroy).grid(row=3,column=0)
#             root_student_name.mainloop()
#
#         Label(frame, text="                          click 4 to get a student report courses", padx=50).grid(row=3,
#                                                                                                            column=0)
#         Button(frame, text="button4", padx=50, command=myclick4).grid(row=3, column=1)
#
#         def myclick5():
#             course_name = input("write the name of the course you want a report for: ")
#             report_and_transcript_maker.create_report_for_a_course(course_name)
#
#         Label(frame, text="          click 5 to get a course report").grid(row=4, column=0)
#         Button(frame, text="button5", padx=50, command=myclick5).grid(row=4, column=1)
#
#         def myclick6():
#             student_name = input("write the name of the student you want a transcript for: ")
#             report_and_transcript_maker.get_transcript(student_name)
#
#         Label(frame, text="    click 6 to get a transcript").grid(row=5, column=0)
#         Button(frame, text="button6", padx=50, command=myclick6).grid(row=5, column=1)
#
#         Button(frame, text="exit", padx=50, command=root.quit).grid(row=7, columnspan=2)
#
#     except ValueError:
#         print("value should be integer")
#     except Exception as e:
#         print(e)
#
#     mainloop()
#
#
# main()

### b. The list of available courses is given in a text file with the following format:
# a. Course number, Name of the course, Course time and days, Number of credits, Course instructor,
# Class location, Course pre-requisite b. The courses are separated by newline
# import os
# from tkinter import *
# from collections import namedtuple
# from curses.ascii import isdigit
#
#
# class Course:
#     def __init__(self, name, time, days, credits, instructor, class_location, pre_requisites):
#         self.name = name
#         self.time = time
#         self.days = days
#         self.credits = credits
#         self.instructor = instructor
#         self.class_location = class_location
#         self.pre_requisite = pre_requisites
#
#
# def create_course_file():
#     course_gui = Tk()
#     course_gui.title("No of course")
#     frame = LabelFrame(course_gui, padx=50, pady=50)
#     frame.pack(padx=50, pady=50)
#     # no_of_available_courses = int(input("how many courses are available?"))
#
#     Label(frame, text="how many courses available? ").pack()
#     e1 = Entry(frame, width=20)
#     e1.pack()
#     courses_file = open("courses_list.txt", "a")
#     def action():
#         for i in range(int(e1.get())):
#             course_gui_2 = Tk()
#             course_gui.title("course details")
#             frame = LabelFrame(course_gui_2, padx=50, pady=50)
#             frame.pack(padx=50, pady=50)
#
#             Label(frame, text="name of course " + str(i + 1) + ": ").pack()
#             e2 = Entry(frame, width=20)
#             e2.pack()
#
#             Label(frame, text="time of course " + str(i + 1) + ": ").pack()
#             e3 = Entry(frame, width=20)
#             e3.pack()
#
#             Label(frame, text="day of course " + str(i + 1) + ": ").pack()
#             e4 = Entry(frame, width=20)
#             e4.pack()
#
#             Label(frame, text="credits of course " + str(i + 1) + ": ").pack()
#             e5 = Entry(frame, width=20)
#             e5.pack()
#
#             Label(frame, text="instructor of course " + str(i + 1) + ": ").pack()
#             e6 = Entry(frame, width=20)
#             e6.pack()
#
#             Label(frame, text="location of course " + str(i + 1) + ": ").pack()
#             e7 = Entry(frame, width=20)
#             e7.pack()
#
#             Label(frame, text="no of prerequisite course " + str(i + 1) + ": ").pack()
#             e8 = Entry(frame, width=20)
#             e8.pack()
#             # course_name = input("what's the name of the course? ")
#             # course_time = input("Time of course " + course_name + ": ")
#             # course_days = input("Days of course " + course_name + ": ")
#             # no_of_credits = int(input("no of credit of course " + course_name + ": "))
#             # course_instructor = input("what's the name of the course instructor of " + course_name + ": ")
#             # class_location = input("write the room no of the course " + course_name + ": ")
#             # no_of_prerequisite_courses = int(input("how many pre-requisite courses for " + course_name + ": "))
#             # enter 0 if there is no pre requisite course
#
#             pre_requisite_courses = ''
#             if int(e8.get()) == 0:
#                 pre_requisite_courses += 'null'
#
#             for j in range(int(e8.get())):
#                 course_gui_3 = Tk()
#                 course_gui.title("course details")
#                 frame = LabelFrame(course_gui_3, padx=50, pady=50)
#                 frame.pack(padx=50, pady=50)
#
#                 Label(frame, text="write the name of " + str(i + 1) + " prerequisite course: ").pack()
#                 d1 = Entry(frame, width=20)
#                 d1.pack()
#                 pre_requisite_courses += d1.get()
#                 if j != int(e8.get()) - 1:
#                     pre_requisite_courses += ','
#             filesize = os.path.getsize("courses_list.txt")
#             if filesize == 0:
#                 courses_file.write(
#                     "course_number: " + str(i + 1) + " course_name: " + e2.get() + " course_time: " + e3.get() +
#                     " course_days: " + e4.get() + " no_of_credits: " + e5.get() + " course_instructor: "
#                     + e6.get() + " class_location: " + e7.get() + " pre-requisite_course: " +
#                     str(pre_requisite_courses) + "\n")
#             else:
#                 x = len(open("courses_list.txt", "r").readlines())
#                 courses_file.write(
#                     "course_number: " + str(i + 1 + x) + " course_name: " + e2.get() + " course_time: " + e3.get() +
#                     " course_days: " + e4.get() + " no_of_credits: " + e5.get() + " course_instructor: "
#                     + e6.get() + " class_location: " + e7.get() + " pre-requisite_course: " +
#                     str(pre_requisite_courses) + "\n")
#
#     Button(frame,text="enter",command=action).pack()
#
#     courses_file.close()
#     course_gui.mainloop()
#
#
# def get_course_details():
#     course_details = []
#     course_file = open("courses_list.txt".strip(), 'r')
#     for line in course_file:
#         line_list = line.split()
#         course_details.append(line_list)
#     course_file.close()
#     return course_details
#
#
# def create_course_object():
#     all_course_objects = []
#     all_courses = get_course_details()
#     course_list = []
#     for i in range(len(all_courses)):
#         course_list.append(all_courses[i][1])
#     for i in range(len(all_courses)):
#         pre_requisites = all_courses[i][15]
#         course_list[i] = Course(all_courses[i][3], all_courses[i][5], all_courses[i][7],
#                                 int(all_courses[i][9]), all_courses[i][11], all_courses[i][13], pre_requisites)
#         all_course_objects.append(course_list[i])
#     return all_course_objects
#
#
# def get_all_courses_with_prerequisite():
#     available_courses_with_prerequisite = {}
#     courses_file = open("courses_list.txt".strip(), "r")
#     course_details_list = []
#     for line in courses_file:
#         line_list = line.split()
#         course_details_list.append(line_list)
#     courses_file.close()
#     for i in range(len(course_details_list)):
#         pre_requisite_list = course_details_list[i][15].split(",")
#         available_courses_with_prerequisite.update({course_details_list[i][3]: pre_requisite_list})
#     return available_courses_with_prerequisite
#

