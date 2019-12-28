import mysql.connector


def insert_new_student(mycursor, mydb):
    first_name = input("Enter student first name: ")
    last_name = input("Enter student last name: ")
    gender = input("Enter student gender: ")

    sql = "SELECT * FROM student WHERE student_first_name = %s AND student_last_name = %s AND student_gender = %s"
    val = [first_name, last_name, gender]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    if len(myresult) > 0:
        print('This student is already in the system.')
    else:
        insert = "INSERT INTO student (student_first_name, student_last_name, student_gender) VALUES (%s, %s, %s)"
        value = (first_name, last_name, gender)
        mycursor.execute(insert, value)
        mydb.commit()
        print('This student is successfully enrolled!')


def insert_new_course(mycursor, mydb):
    course_title = input("Enter course title: ")
    sql = "SELECT * FROM course WHERE course_title = %s"
    val = [course_title]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    if len(myresult) > 0:
        print('This course is already in the system.')
    else:
        other_time = input("Do you want to add weekdays for this course? ")
        while other_time.lower() == "yes":

            course_day = input("Enter the weekday of this course (Monday-Sunday): ")
            while course_day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                course_day = input("Wrong weekday input! Enter the weekday of this course (Monday-Sunday): ")
            course_time = input("Enter what time will this course be: ")
            sql = "INSERT INTO course (course_title) VALUES (%s)"
            val = [course_title]
            mycursor.execute(sql, val)
            sql2 = "INSERT INTO course_details (course_id, weekday, class_time) SELECT course_id, %s, %s FROM " \
                   "course LEFT JOIN course_details USING (course_id) WHERE course_title = %s"
            val2 = [course_day, course_time, course_title]
            mycursor.execute(sql2, val2)
            mydb.commit()
            print("This course is successfully introduced")
            other_time = input("Does this course have other time on another day? (Yes/No)")
        # other_time = input("Does this course have other time on another day? (Yes/No)")
        # while other_time.lower() == "yes":
        #
        # print("This course is successfully introduced")


def enroll_course(mycursor, mydb):
    student_id = input("Enter the student ID: ")
    sql = "SELECT * FROM student WHERE student_id = %s"
    val = [student_id]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        print("Student not in the system, enroll this new student first")
    else:
        course_id = input("Enter the course ID enroll: ")
        registered = "SELECT * FROM student_course WHERE student_id = %s AND course_id = %s"
        val = [student_id, course_id]
        mycursor.execute(registered, val)
        result = mycursor.fetchall()

        if len(result) > 0:
            print("This student has already registered for this course")
        else:
            sql = "INSERT INTO student_course (student_id, course_id) VALUES (%s, %s)"
            val = [student_id, course_id]
            mycursor.execute(sql, val)
            mydb.commit()
            print("This student successfully enrolled in this course")


def check_students(mycursor, mydb):
    course_id = input("Enter the course ID that you want to check that what students are enrolled: ")
    sql = "SELECT * FROM course WHERE course_id = %s"
    val = [course_id]
    mycursor.execute(sql, val)
    result = mycursor.fetchall()

    if len(result) == 0:
        print("Course ID entered is invalid")
    else:
        sql = "SELECT CONCAT(student_first_name, ' ', student_last_name) AS student_full_name " \
              "FROM student JOIN student_course USING (student_id) JOIN course USING (course_id)" \
              "WHERE course_id = %s"
        val = [course_id]
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        print("The following students are in this class")
        for i in result:
            print(i)


def check_courses(mycursor, mydb):
    student_id = input("Enter the student ID: ")
    sql = "SELECT * FROM student WHERE student_id = %s"
    val = [student_id]
    mycursor.execute(sql, val)
    result = mycursor.fetchall()

    if len(result) == 0:
        print("Student ID entered is invalid")
    else:
        sql = "SELECT course_title " \
              "FROM student JOIN student_course USING (student_id) JOIN course USING (course_id)" \
              "WHERE student_id = %s"
        val = [student_id]
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        print("This student is enrolled in the following classes")
        for i in result:
            print(i)


def check_weekday_courses(mycursor, mydb):
    student_id = input("Enter the student ID: ")
    sql = "SELECT * FROM student WHERE student_id = %s"
    val = [student_id]
    mycursor.execute(sql, val)
    result = mycursor.fetchall()

    if len(result) == 0:
        print("Student ID entered is invalid")
    else:
        weekday = input("Enter the weekday (monday - sunday): ").lower()
        while weekday not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            weekday = input("Wrong weekday input! Enter the weekday of this course (monday-sunday): ")

        sql = "SELECT CONCAT('course title: ', course_title, ', time: ', class_time) AS schedule " \
              "FROM student JOIN student_course USING (student_id) JOIN course USING (course_id) JOIN course_details USING (course_id)" \
              "WHERE student_id = %s AND weekday REGEXP %s"
        val = [student_id, weekday]
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        if len(result) == 0:
            print("This student does not have class on", weekday)
        else:
            print("The class schedule for this student on", weekday, "is: ")
            for i in result:
                print(i)


mydb = mysql.connector.connect(host="localhost", user="root", passwd="fwh3838438", database="StudentEnrollment")
mycursor = mydb.cursor()

print("Welcome to Student Enrollment System!")

while True:
    print("====================================================================================================")
    print("1: add new student \n"
          "2: add new course \n"
          "3: enroll course \n"
          "4: check students in a course \n"
          "5: check all the courses that a student enrolled \n"
          "6: check which courses and what times each course is for a given student on a given day of the week \n"
          "7: quit this program")
    instruction = input("Please type your instruction: ")
    if instruction == "1":
        insert_new_student(mycursor, mydb)
    elif instruction == "2":
        insert_new_course(mycursor, mydb)
    elif instruction == "3":
        enroll_course(mycursor, mydb)
    elif instruction == "4":
        check_students(mycursor, mydb)
    elif instruction == "5":
        check_courses(mycursor, mydb)
    elif instruction == "6":
        check_weekday_courses(mycursor, mydb)
    elif instruction == "7":
        exit(0)
    else:
        print("Wrong instruction!")
