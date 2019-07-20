import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");


conn.execute('''CREATE TABLE IF NOT EXISTS STUDENTINFO
         (ROLLNO     INT  PRIMARY KEY NOT NULL,
         RANK        NOT NULL,
         NAME        TEXT,
         EMAIL       TEXT,
         GENDER      TEXT,
         STATE       TEXT,
         CATEGORY    TEXT,
         BOARD       TEXT,
         SCHOOL      TEXT,
         PERCENTAGE  INT);''')
print ("STUDENTINFO Table created successfully");
cursor1 =conn.execute("SELECT ROLLNO,RANK,NAME,EMAIL,GENDER,STATE,CATEGORY,BOARD,SCHOOL,PERCENTAGE FROM STUDENTINFO")


conn.execute('''CREATE TABLE IF NOT EXISTS SEATINFO
         (ROLLNO     INT,
         RANK        INT,
         CRANK       INT,
         COLLEGE     TEXT,
         BRANCH      TEXT,
         SEATS       INT);''')
print ("SEATINFO Table created successfully");
cursor2 =conn.execute("SELECT ROLLNO,RANK,CRANK,COLLEGE,BRANCH,SEATS FROM SEATINFO")


conn.execute('''CREATE TABLE IF NOT EXISTS COLLEGEINFO
         (CRANK       INT,
         COLLEGE     TEXT,
         BRANCH      TEXT,
         SEATS       INT);''')

def insert():
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (1,'IIT DELHI','COMPUTER SCIENCE',2)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (2,'IIT GUWAHATI','COMPUTER SCIENCE',3)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
     VALUES (3,'NIT KURUKSHETRA','INFORMATION TECHNOLOGY',2)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (4,'IIT DELHI','BIOTECHNOLOGY',1)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (5,'NIT KURUKSHETRA','COMPUTER SCIENCE',2)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (6,'IIT GUWAHATI','MECHANICAL ENGINEERING',1)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (7,'IIT DELHI','MECHANICAL ENGINNERING',4)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (8,'NIT KURUKSHETRA','ELECTRONICS',1)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (9,'NIT KURUKSHETRA','MECHANICAL ENGINEERING',3)");
 conn.execute("INSERT INTO COLLEGEINFO (CRANK,COLLEGE,BRANCH,SEATS) \
      VALUES (10,'IIT PATNA','CIVIL ENGINEERING',2)");
 print ("COLLEGEINFO ENTRIES created successfully");

insert()
cursor3 =conn.execute("SELECT CRANK,COLLEGE,BRANCH,SEATS FROM COLLEGEINFO")


conn.execute('''CREATE TABLE IF NOT EXISTS CHOICEINFO
         (ROLLNO       INT,
         CRANK        INT,
         COLLEGE     TEXT,
         BRANCH      TEXT,
         SEATS       INT);''')
print ("CHOICEINFO Table created successfully");
cursor4 =conn.execute("SELECT ROLLNO,CRANK,COLLEGE,BRANCH,SEATS FROM CHOICEINFO")


print("################################################")
for row in cursor1:
   for i in row:
      print(i)
   print("-------------")
print ("STUDENTINFO Data printed successfully")

print("################################################")
for row in cursor2:
   for i in row:
      print(i)
   print("-------------")
print ("SEATINFO Data printed successfully")

print("################################################")
for row in cursor3:
   print(row[0]," ",row[1]," ",row[2]," ",row[3])
print ("COLLEGEINFO Data printed successfully")

print("################################################")
for row in cursor4:
   for i in row:
      print(i)
   print("-------------")
print ("CHOICEINFO Data printed successfully")
conn.commit()
conn.close()
