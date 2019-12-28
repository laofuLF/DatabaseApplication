USE StudentEnrollment;

DROP TABLE IF EXISTS course_details;
DROP TABLE IF EXISTS student_course;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS course;



CREATE TABLE student
(
  student_id     		INT           PRIMARY KEY   AUTO_INCREMENT,
  student_first_name    VARCHAR(50)   NOT NULL,
  student_last_name     VARCHAR(50)   NOT NULL,
  student_gender        VARCHAR(50)   NOT NULL
) AUTO_INCREMENT = 10000;

CREATE TABLE course
(
  course_id     		INT           PRIMARY KEY   AUTO_INCREMENT,
  course_title    		VARCHAR(50)   NOT NULL
) AUTO_INCREMENT = 20000;

CREATE TABLE student_course (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    CONSTRAINT student_course_fk_student FOREIGN KEY (student_id)
        REFERENCES student (student_id),
    CONSTRAINT student_course_fk_course FOREIGN KEY (course_id)
        REFERENCES course (course_id)
);

CREATE TABLE course_details (
	course_id			INT 			NOT NULL,
    weekday				VARCHAR(50)		NOT NULL,
    class_time			VARCHAR(50)		NOT NULL,
	CONSTRAINT course_detail_fk_course_id FOREIGN KEY (course_id)
        REFERENCES course (course_id)
);



