from tkinter import *
import admin
import courses
import student
from admin import Admin
import report_and_transcript_maker
from tkinter import filedialog


def main():
    root = Tk()
    root.title("Menu")
    frame = LabelFrame(root,padx=50,pady=50)
    frame.pack(padx=50,pady=50)
    try:
        def myclick1():
            root_create_course = Tk()
            frame = Frame(root_create_course, padx=30, pady=30)
            frame.pack()
            Label(frame, text="your course/courses details have been added").pack()
            courses.create_course_file()

        Label(frame, text="           To create a course file").grid(row=0, column=0)
        Button(frame, text="button1", padx=50, command=myclick1).grid(row=0, column=1)

        def myclick2():
            show_all_available_courses = Tk()
            show_all_available_courses.title("All the available courses")
            frame = LabelFrame(show_all_available_courses, padx=50, pady=50)
            frame.pack(padx=100, pady=100)
            course_file = open("courses_list.txt", "r")
            Label(frame, text=course_file.read()).grid(row=0, column=0)
            course_file.close()
            show_all_available_courses.mainloop()

        Label(frame, text="       To show all courses").grid(row=1, column=0)
        Button(frame, text="button2", padx=50, command=myclick2).grid(row=1, column=1)

        def myclick3():
            root_add_student = Tk()
            frame = Frame(root_add_student, padx=30, pady=30)
            frame.pack(padx=100, pady=100)
            Label(frame, text="student/students details have been added").pack()
            student.create_student_file()

        Label(frame, text=" To add students").grid(row=2, column=0)
        Button(frame, text="button3", padx=50, command=myclick3).grid(row=2, column=1)

        def myclick4():
            show_all_students = Tk()
            show_all_students.title("All the available courses")
            frame = LabelFrame(show_all_students, padx=50, pady=50)
            frame.pack(padx=100, pady=100)
            student_file = open("student.txt", "r")
            Label(frame, text=student_file.read()).grid(row=0, column=0)
            student_file.close()
            show_all_students.mainloop()

        Label(frame, text="         To show all students").grid(row=3, column=0)
        Button(frame, text="button4", padx=50, command=myclick4).grid(row=3, column=1)

        def myclick5():
            root_register_student = Tk()
            frame = Frame(root_register_student, padx=30, pady=30)
            frame.pack(padx=100, pady=100)
            Label(frame, text="student/students have been registered").pack()
            admin1 = Admin()
            admin1.register_all_student(admin.get_upcoming_register_student_with_subject_list())

        Label(frame, text="             To register all students").grid(row=4, column=0)
        Button(frame, text="button5", padx=50, command=myclick5).grid(row=4, column=1)

        def myclick6():
            root_student_name = Tk()
            root_student_name.title("Get a report")

            frame = LabelFrame(root_student_name,padx=20,pady=20)
            frame.pack(padx=100,pady=100)
            Label(frame, text="enter the accurate student name").grid(row=0,column=0)
            e = Entry(frame, width=50)
            e.grid(row=1,column=0)

            def inner_click():
                report_and_transcript_maker.create_report_for_a_student(e.get())
                show_report = Tk()
                show_report.title("Report of the given student")
                frame = LabelFrame(show_report,padx=10,pady=10)
                frame.pack(padx=100,pady=100)
                student_file = open("student_report.txt", "r")
                Label(frame, text=student_file.read()).grid(row=0,column=0)
                student_file.close()
                show_report.mainloop()

            Button(frame, text="enter", command=inner_click).grid(row=2,column=0)
            Button(frame, text="go back", command=root_student_name.destroy).grid(row=3,column=0)
            root_student_name.mainloop()

        Label(frame, text="              To get a student report", padx=50).grid(row=5,
                                                                                                           column=0)
        Button(frame, text="button6", padx=50, command=myclick6).grid(row=5, column=1)

        def myclick7():
            root_course_name = Tk()
            root_course_name.title("Get a report")
            frame = LabelFrame(root_course_name, padx=20, pady=20)
            frame.pack(padx=100, pady=100)
            Label(frame, text="enter the valid course name").grid(row=0, column=0)
            e = Entry(frame, width=50)
            e.grid(row=1, column=0)

            def inner_click():
                report_and_transcript_maker.create_report_for_a_course(e.get())
                show_report = Tk()
                show_report.title("Report of the given course")
                frame = LabelFrame(show_report, padx=10, pady=10)
                frame.pack(padx=100, pady=100)
                course_file = open("course_report.txt", "r")
                Label(frame, text=course_file.read()).grid(row=0, column=0)
                course_file.close()
                show_report.mainloop()

            Button(frame, text="enter", command=inner_click).grid(row=2, column=0)
            Button(frame, text="go back", command=root_course_name.destroy).grid(row=3, column=0)
            root_course_name.mainloop()

        Label(frame, text="            To get a course report").grid(row=6, column=0)
        Button(frame, text="button7", padx=50, command=myclick7).grid(row=6, column=1)

        def myclick8():
            root_student_name = Tk()
            root_student_name.title("Get a report")

            frame = LabelFrame(root_student_name, padx=20, pady=20)
            frame.pack(padx=100, pady=100)
            Label(frame, text="enter the accurate student name").grid(row=0, column=0)
            e = Entry(frame, width=50)
            e.grid(row=1, column=0)

            def inner_click():
                report_and_transcript_maker.get_transcript(e.get())
                show_transcript = Tk()
                show_transcript.title("Report of the given student")
                frame = LabelFrame(show_transcript, padx=10, pady=10)
                frame.pack(padx=100, pady=100)
                transcript_file = open("transcripts.txt", "r")
                Label(frame, text=transcript_file.read()).grid(row=0, column=0)
                transcript_file.close()
                show_transcript.mainloop()

            Button(frame, text="enter", command=inner_click).grid(row=2, column=0)
            Button(frame, text="go back", command=root_student_name.destroy).grid(row=3, column=0)
            root_student_name.mainloop()

        Label(frame, text="      To get a transcript").grid(row=7, column=0)
        Button(frame, text="button8", padx=50, command=myclick8).grid(row=7, column=1)

        Button(frame, text="exit", padx=50, command=root.quit).grid(row=8, columnspan=2)

    except ValueError:
        print("value should be integer")
    except Exception as e:
        print(e)

    mainloop()


main()
