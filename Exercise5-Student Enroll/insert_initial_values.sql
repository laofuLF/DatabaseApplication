USE StudentEnrollment;

INSERT INTO student VALUES
	(DEFAULT, "Yiling", "Wang", "male"),
	(DEFAULT, "Xizi", "Wang", "female"),
	(DEFAULT, "Soobin", "Choi", "female"),
	(DEFAULT, "Jing", "Cheng", "female"),
	(DEFAULT, "Xiaolue", "Peng", "male"),
	(DEFAULT, "Xiling", "Li", "female"),
	(DEFAULT, "Weihuan", "Fu", "male"),
	(DEFAULT, "Zeyu", "Huang", "male"),
	(DEFAULT, "Aman", "Bhatia", "male");
    
INSERT INTO course VALUES
	(DEFAULT, "Data Structure and Algorithm"),
	(DEFAULT, "Java Concurrency"),
	(DEFAULT, "Database MySQL"),
	(DEFAULT, "Mobile Programming"),
	(DEFAULT, "Information data retrieval");
    
INSERT INTO course_details VALUES
	(20000, "Monday", "8:30 - 9:30"),
    (20000, "Tuesday", "8:30 - 9:30"),
    (20001, "Wednesday", "13:30 - 15:30"),
    (20001, "Tuesday", "13:30 - 15:30"),
    (20002, "Friday", "12:30 - 13:30"),
    (20003, "Tuesday", "9:30 - 10:30"),
    (20004, "Thursday", "14:30 - 15:30");
    
INSERT INTO student_course VALUES
	(10000, 20001),
    (10000, 20003),
    (10001, 20002),
    (10002, 20003),
    (10003, 20001),
    (10006, 20002);



	
