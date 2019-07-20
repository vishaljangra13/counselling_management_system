from tkinter import *
from tkinter import messagebox
import sqlite3
def raise_frame(frame):
    frame.tkraise()
    
def database1():
    global rollno2,rank2
    rollno2 = rollno1.get()
    rank2 = rank1.get()
    rank3=rank2
    conn = sqlite3.connect('database.db')
    with conn:
      cursor = conn.cursor()
    va=cursor.execute("SELECT * FROM SEATINFO WHERE ROLLNO=?",(rollno2,))
    va2=(list)(va)
    va5=cursor.execute("SELECT * FROM SEATINFO")
    va6=(list)(va)
    if (len(va6)==0) or not(len(va2)==0):
        cursor.execute("""INSERT INTO STUDENTINFO(ROLLNO,RANK) SELECT ?,? WHERE NOT EXISTS(SELECT ROLLNO FROM STUDENTINFO WHERE ROLLNO=?)""",(rollno2,rank2,rollno2))
        val = cursor.execute("SELECT RANK FROM STUDENTINFO WHERE ROLLNO=?",(rollno2,))
        val1=(list)(val)
        rank2=val1[0][0]
        va3=cursor.execute("SELECT ROLLNO,RANK FROM STUDENTINFO WHERE ROLLNO=?",(rollno2,))
        va4=(list)(va3)
        if(va4[0][1]==rank3):
            Label(framec0_1,text="Roll No: "+(str)(rollno2),bg='black',fg='white',font=("bold",20),justify=LEFT).place(y=0)
            Label(framec0_1,text="Rank: "+(str)(rank2),bg='black',fg='white',font=("bold",20),justify=RIGHT).place(x=450,y=0)
            raise_frame(pagec0)
        else:
            messagebox.showinfo("Alert","""You entered different details than the one that you used first time for login,Please try again!""")
    else:
        messagebox.showinfo("Alert","""You cannot login with new username and password once the result is generated!""")
    conn.commit()
    conn.close()

def database2():
  name2=name1.get()
  email2=email1.get()
  gender2=gender1.get()
  state2=state1.get()
  category2=category1.get()
  school2=school1.get()
  percentage2=percentage1.get()
  board2=board1.get()
  rollno2=rollno1.get()
  conn = sqlite3.connect('database.db')
  with conn:
      cursor = conn.cursor()
      cursor.execute('''UPDATE STUDENTINFO SET NAME=?,EMAIL=?,GENDER=?,STATE=?,CATEGORY=?,BOARD=?,SCHOOL=?,PERCENTAGE=? WHERE
                            ROLLNO=?''',(name2,email2,gender2,state2,category2,board2,school2,percentage2,rollno2))
      conn.commit()
  conn.close()
  Label(framec3_1,text="Roll No: "+(str)(rollno2),bg='black',fg='white',font=("bold",20),justify=LEFT).place(y=0)
  Label(framec3_1,text="Rank: "+(str)(rank2),bg='black',fg='white',font=("bold",20),justify=RIGHT).place(x=450,y=0)
  raise_frame(pagec3)

def database3():
    global varplace,indexplace
    college2=(str)(college1.get())
    college3=(college2[1:-1]).split(',')
    college3[1]=college3[1][2:-1]
    college3[2]=college3[2][2:-1]
    rollno2=rollno1.get()
    varplace+=20
    indexplace+=1
    rollno2=rollno1.get()
    conn = sqlite3.connect('database.db')
    with conn:
      cursor = conn.cursor()
    cursor.execute('INSERT INTO CHOICEINFO(ROLLNO,CRANK,COLLEGE,BRANCH,SEATS) VALUES(?,?,?,?,?)',(rollno2,(int)(college3[0]),college3[1],college3[2],(int)(college3[3])))
    conn.commit()
    conn.close()
    Label(framec3_2, text=(str)(indexplace)+")  "+college3[1]+"     "+college3[2],width=45,bg='green',fg='white',font=("bold", 12),anchor='w').place(x=100,y=210+varplace)
    

def box():
    messagebox.showinfo("Final Submit","Your registration has been completed.Please wait while result is generated!")
    raise_frame(home)

def fun1():
    conn = sqlite3.connect('database.db')
    with conn:
      cursor = conn.cursor()
    var = cursor.execute('SELECT * FROM CHOICEINFO WHERE ROLLNO=?',(rollno2,))
    var1 =(list)(var)
    if not(len(var1)==0):
        messagebox.showinfo("Acess Denied","""You cannot make changes since your application has already been completed.Kindly check results!""")
    else:
        Label(framec2_1,text="Roll No: "+(str)(rollno2),bg='black',fg='white',font=("bold",20),justify=LEFT).place(y=0)
        Label(framec2_1,text="Rank: "+(str)(rank2),bg='black',fg='white',font=("bold",20),justify=RIGHT).place(x=450,y=0)
        raise_frame(pagec2)

def fun2():
    admin3 = admin1.get()
    admin4 = admin2.get()
    if (admin3 == 'tarunbhati' and admin4 == 'IT_11710528'):
        messagebox.showinfo("Acess Granted","""Welcome,Access has been granted!""")
        raise_frame(pagea1)
    else:
        messagebox.showinfo("Acess Denied","""You tried to access using invalid username and password!Kindly make sure that you are an admin before login!""")

def fun3():
    messagebox.showinfo("Log Out","""You have been successfully logged out!""")
    raise_frame(pagea0)

def generate_result():
    conn = sqlite3.connect('database.db')
    with conn:
      cursor = conn.cursor()
    v = cursor.execute('SELECT * FROM SEATINFO')
    v1=(list)(v)
    if not(len(v1)==0):
      messagebox.showinfo("Result Generated!","You cannot generate result twice!")
    else:
        #
      var = cursor.execute('SELECT ROLLNO,CRANK,COLLEGE,BRANCH,SEATS,RANK,PERCENTAGE FROM CHOICEINFO NATURAL JOIN STUDENTINFO ORDER BY RANK,PERCENTAGE DESC')
      var1 =(list)(var)
      #print("===========================")
      i=0
      while(i<len(var1)):
        list1=[]
        val=var1[i][0]
        for j in range(i,len(var1)):
            if(val==var1[j][0]):
                list1.append(var1[j])
                i=i+1
        #print("\n\n\n",list1)
        var3=[]
        for k in range(0,len(list1)):
            var2 = cursor.execute('SELECT * FROM COLLEGEINFO WHERE CRANK=? AND NOT(SEATS==0)',(list1[k][1],))
            var3=(list)(var2)
            if not(len(var3)==0):
                break
        #print("\n",var3)
        if not(len(var3)==0):
            conn.execute("INSERT INTO SEATINFO (ROLLNO,RANK,CRANK,COLLEGE,BRANCH,SEATS) \
                         VALUES (?,?,?,?,?,?)",(list1[0][0],list1[0][5],var3[0][0],var3[0][1],var3[0][2],var3[0][3]));
            va = cursor.execute('SELECT SEATS FROM COLLEGEINFO WHERE CRANK=?',(var3[0][0],))
            va2=(list)(va)
            va3=va2[0][0]-1
            if(va3<0):
                va3=0
            conn.execute("UPDATE COLLEGEINFO SET SEATS=? WHERE CRANK=?",(va3,var3[0][0]));
        else:
            conn.execute("INSERT INTO SEATINFO (ROLLNO,RANK,CRANK,COLLEGE,BRANCH,SEATS) \
                         VALUES (?,?,0,0,0,0)",(list1[0][0],list1[0][5]));       
      conn.commit()
      conn.close()
      messagebox.showinfo("Result Generated!","The result has been successfully generated.Kindly click on view overall result to view.")

def view_overallresult():
    ind1,ind2=0,0
    list1=[10,50,30,5,20,20]
    list2=['black','green','black','green','black','green']
    list3=[10,100,205,265,330,505]
    list4=['ROLLNO','NAME','RANK','%AGE','College','Branch']
    raise_frame(pagea2)
    conn = sqlite3.connect('database.db')
    cursor =conn.execute("SELECT ROLLNO,NAME,RANK,PERCENTAGE,COLLEGE,BRANCH FROM SEATINFO NATURAL JOIN STUDENTINFO")
    for ind2 in range(0,6):
         Label(framea2_1,text=list4[ind2],bg='white',fg='black',width=list1[ind2],font="Times,10,bold",anchor='w').place(x=list3[ind2],y=140)
    cursor =conn.execute("SELECT ROLLNO,NAME,RANK,PERCENTAGE,COLLEGE,BRANCH FROM SEATINFO NATURAL JOIN STUDENTINFO")
    for i in cursor:
         ind2=0
         for j in i:
              Label(framea2_1,text=j,bg=list2[ind2],fg='white',width=list1[ind2],font="Times,5,bold",anchor='w').place(x=list3[ind2],y=170+ind1*23)
              ind2+=1
         ind1+=1
    conn.commit()
    conn.close()


def box2():
    conn = sqlite3.connect('database.db')
    with conn:
      cursor = conn.cursor()
      val = cursor.execute("SELECT * FROM SEATINFO")
      val1 = (list)(val)
      if(len(val1)==0):
          messagebox.showinfo("View Result","Results are not out yet.Please wait while we generate result")
      else:
          messagebox.showinfo("View Result","Results has been declared,click okay to view!")
          va = cursor.execute("SELECT * FROM SEATINFO WHERE ROLLNO=?",(rollno2,))
          va2=(list)(va)
          if(va2[0][2]==0):
              Label(framec5_1,text="""Sorry,No seat has been alloted to you based
on your JEC Rank and Board percentage!""",bg='pink',fg='white',height=20,width=45,font=("bold",20),anchor='n').place(x=10,y=150)
          else:
              ind2=0
              list2=['black','red','black','red']
              list4=['   ROLL NO:','   RANK:','   COLLEGE ALLOTED:','   BRANCH ALLOTED:']
              Label(framec5_1,text="""Congratulations!
You have been alloted the following seat
based on your JEC Rank and Board percentage:""",bg='pink',fg='white',height=20,width=45,font=("bold",20),anchor='n').place(x=5,y=150)
              conn = sqlite3.connect('database.db')
              cursor =conn.execute("SELECT ROLLNO,RANK,COLLEGE,BRANCH FROM SEATINFO WHERE ROLLNO=?",(rollno2,))
              for i in range(0,4):
                  Label(framec5_1,text=list4[i],bg=list2[i],fg='white',width=50,font="Times,5,bold",anchor='w').place(x=40,y=300+i*40)
              for i in cursor:
                  ind2=0
                  for j in i:
                      Label(framec5_1,text=j,bg=list2[ind2],fg='white',width=30,font="Times,5,bold",anchor='w').place(x=400,y=300+ind2*40)
                      ind2+=1
          conn.commit()
          conn.close() 
          raise_frame(pagec5)
    
    

       
root = Tk()
root.geometry('700x1000')
root.title("JEC - 2019")

rollno1 = IntVar()
rank1 = IntVar()
name1=StringVar()
email1=StringVar()
gender1=StringVar()
state1=StringVar()
category1=StringVar()
school1=StringVar()
percentage1=IntVar()
board1=StringVar()
admin1= StringVar()
admin2= StringVar()
####################################################HOME
home = Frame(root,width=700,height=1000,bg='red')
home.grid(row=0,column=0,sticky='news')

frame0 = Frame(home,bg='blue',height=150,width=700)
frame0.pack()
frame1 = Frame(home,bg='white',height=850,width=700)
frame1.pack()

label_0 = Label(frame0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35))
label_0.place(x=20,y=20)
label_1 = Label(frame0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20))
label_1.place(x=20,y=80)

Label(frame1,text="""HOME
The Joint Seat Allocation Authority (JoSAA) 2018 has been set up by
the Ministry of Human Resources Development (MHRD)to manage and
regulate the joint seat allocation for admissions to 100 institutes
for the academic year 2018-19. This includes 23 IITs,31 NITs and 23
IIITs. Admission to all the academic programs offered by these
Institutes will be made through a single platform.""",bg="white",font=('bold',15),justify=LEFT).place(x=50,y=50)
button1 = Button(frame1, text="Login as Admin",width=32,bg='brown',fg='white',font=('bold',20),command=lambda:raise_frame(pagea0))
button1.place(x=100,y=280)
button2 = Button(frame1, text="View Seat Matrix",width=32,bg='brown',fg='white',font=('bold',20),command=lambda:raise_frame(pageb))
button2.place(x=100,y=350)
button3 = Button(frame1, text="Login as Student to apply for counselling",width=32,bg='brown',fg='white',font=('bold',20),command=lambda:raise_frame(pagec1))
button3.place(x=100,y=420)

####################################################PAGEA


####################################################PAGEA0
pagea0 = Frame(root,width=700,height=1000,bg='red')
pagea0.grid(row=0,column=0,sticky='news')

framea0_0 = Frame(pagea0,bg='blue',height=150,width=700)
framea0_0.pack()
framea0_1 = Frame(pagea0,bg='pink',height=850,width=700)
framea0_1.pack()

Label(framea0_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35)).place(x=20,y=20)
Label(framea0_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20)).place(x=20,y=80)

Button(framea0_1, text='<--Back',width=10,bg='brown',fg='white',command=lambda:raise_frame(home)).place(x=10,y=10)
Label(framea0_1, text="LOGIN AS ADMIN",font=("bold", 20),bg='pink').place(x=220,y=53)
Label(framea0_1, text="(Login Only if you have valid username and password)",font=(20),bg='pink').place(x=150,y=83)
framea0_2 = Frame(framea0_1,bg='green',height=300,width=500)
framea0_2.place(x=100,y=150)
labela0_1 = Label(framea0_2, text="UserName :",bg='green',fg='white',font=("bold", 20))
labela0_1.place(x=50,y=80)
entrya0_1 = Entry(framea0_2,width=30,textvar = admin1)
entrya0_1.place(x=240,y=92)
labela0_2 = Label(framea0_2, text="Password  :",bg='green',fg='white',font=("bold", 20))
labela0_2.place(x=50,y=130)
entrya0_2 = Entry(framea0_2,width=30,textvar = admin2)
entrya0_2.place(x=240,y=142)
Button(framea0_2, text='Submit',width=20,bg='black',fg='white',command=fun2).place(x=180,y=200)






####################################################PAGEA1
pagea1 = Frame(root,width=700,height=1000,bg='red')
pagea1.grid(row=0,column=0,sticky='news')

framea1_0 = Frame(pagea1,bg='blue',height=150,width=700)
framea1_0.pack()
framea1_2 = Frame(pagea1,bg='pink',height=1000,width=700)
framea1_2.pack()

Label(framea1_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35)).place(x=20,y=20)
Label(framea1_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20)).place(x=20,y=80)

Button(framea1_2, text='Generate Result',width=20,bg='brown',fg='white',font=("bold",30),command=generate_result).place(x=100,y=100)
Button(framea1_2, text='View Overall Result',width=20,bg='brown',fg='white',font=("bold",30),command=view_overallresult).place(x=100,y=200)
Button(framea1_2, text='Log Out',width=10,bg='black',fg='white',font=("bold",30),command=fun3).place(x=200,y=300)



####################################################PAGEA2
pagea2 = Frame(root,width=700,height=1000,bg='red')
pagea2.grid(row=0,column=0,sticky='news')


framea2_0 = Frame(pagea2,bg='blue',height=150,width=700)
framea2_0.pack()
framea2_1 = Frame(pagea2,bg='PINK',height=850,width=700)
framea2_1.pack()

labela2_0 = Label(framea2_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35))
labela2_0.place(x=20,y=20)
labela2_1 = Label(framea2_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20))
labela2_1.place(x=20,y=80)


Button(framea2_1, text="<--Back",width=10,bg='brown',fg='white',command=lambda:raise_frame(pagea1)).place(x=5,y=5)
Label(framea2_1,text="OVERALL RESULT OF JEC",bg='red',fg='yellow',font=("bold",25)).place(x=150,y=60)



####################################################PAGEB

pageb = Frame(root,width=700,height=1000,bg='red')
pageb.grid(row=0,column=0,sticky='news')
ind1,ind2=0,0
list1=[5,30,30,5]
list2=['black','red','black','red']
list3=[75,125,325,575]
list4=['CRank','College Name','Branch','Seats']

frameb_0 = Frame(pageb,bg='blue',height=150,width=700)
frameb_0.pack()
frameb_1 = Frame(pageb,bg='white',height=850,width=700)
frameb_1.pack()

labelb_0 = Label(frameb_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35))
labelb_0.place(x=20,y=20)
labelb_1 = Label(frameb_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20))
labelb_1.place(x=20,y=80)


Button(frameb_1, text="<--Back",width=10,bg='brown',fg='white',command=lambda:raise_frame(home)).place(x=5,y=5)
Label(frameb_1,text="JOINT EXAM COLLEGE  SEATS MATRIX",bg='green',fg='yellow',font=("bold",25)).place(x=30,y=60)
conn = sqlite3.connect('database.db')
cursor =conn.execute("SELECT CRANK,COLLEGE,BRANCH,SEATS FROM COLLEGEINFO")
for ind2 in range(0,4):
    Label(frameb_1,text=list4[ind2],bg='pink',fg='black',width=list1[ind2],font="Times,10,bold",anchor='w').place(x=list3[ind2],y=140)
cursor =conn.execute("SELECT CRANK,COLLEGE,BRANCH,SEATS FROM COLLEGEINFO")
for i in cursor:
    ind2=0
    for j in i:
        Label(frameb_1,text=j,bg=list2[ind2],fg='white',width=list1[ind2],font="Times,5,bold",anchor='w').place(x=list3[ind2],y=170+ind1*20)
        ind2+=1
    ind1+=1
conn.commit()
conn.close()


####################################################PAGEC

####################################################PAGEC1

pagec1 = Frame(root,width=700,height=1000,bg='red')
pagec1.grid(row=0,column=0,sticky='news')

framec1_0 = Frame(pagec1,bg='blue',height=150,width=700)
framec1_0.pack()
framec1_1 = Frame(pagec1,bg='white',height=850,width=700)
framec1_1.pack()
framec1_2 = Frame(framec1_1,bg='black',height=300,width=500)
framec1_2.place(x=100,y=150)

Button(framec1_1, text='<--Back',width=10,bg='brown',fg='white',command=lambda:raise_frame(home)).place(x=10,y=10)
Label(framec1_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35)).place(x=20,y=20)
Label(framec1_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20)).place(x=20,y=80)

Label(framec1_1, text="LOGIN AS STUDENT",font=("bold", 20),bg='white').place(x=220,y=53)
Label(framec1_1, text="(Use Your JEC Roll No As Username And Rank as Password)",font=(20),bg='white').place(x=150,y=83)

label_1 = Label(framec1_2, text="UserName :",bg='black',fg='white',font=("bold", 20))
label_1.place(x=50,y=80)
entry_1 = Entry(framec1_2,width=30,textvar = rollno1)
entry_1.place(x=240,y=92)
label_2 = Label(framec1_2, text="Password  :",bg='black',fg='white',font=("bold", 20))
label_2.place(x=50,y=130)
entry_2 = Entry(framec1_2,width=30,textvar = rank1)
entry_2.place(x=240,y=142)

Button(framec1_2, text='Submit',width=20,bg='brown',fg='white',command=database1).place(x=180,y=200)






####################################################PAGEC0

pagec0 = Frame(root,width=700,height=1000,bg='red')
pagec0.grid(row=0,column=0,sticky='news')

framec0_0 = Frame(pagec0,bg='blue',height=150,width=700)
framec0_0.pack()
framec0_1 = Frame(pagec0,bg='black',height=50,width=700)
framec0_1.pack()
framec0_2 = Frame(pagec0,bg='pink',height=1000,width=700)
framec0_2.pack()

Label(framec0_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35)).place(x=20,y=20)
Label(framec0_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20)).place(x=20,y=80)
Label(framec0_1,text="Roll No: ",bg='black',fg='white',font=("bold",20),justify=LEFT).place(y=0)
Label(framec0_1,text="Rank: ",bg='black',fg='white',font=("bold",20),justify=RIGHT).place(x=450,y=0)
Button(framec0_2, text='Proceed to fill details',width=20,bg='brown',fg='white',font=("bold",30),command=fun1).place(x=100,y=100)
Button(framec0_2, text='View Result',width=20,bg='brown',fg='white',font=("bold",30),command=box2).place(x=100,y=200)
Button(framec0_2, text='Log Out',width=10,bg='black',fg='white',font=("bold",30),command=lambda:raise_frame(pagec1)).place(x=200,y=300)





###################################################PAGEC2

pagec2 = Frame(root,width=700,height=1000,bg='red')
pagec2.grid(row=0,column=0,sticky='news')

framec2_0 = Frame(pagec2,bg='blue',height=150,width=700)
framec2_0.pack()
framec2_1 = Frame(pagec2,bg='black',height=50,width=700)
framec2_1.pack()
framec2_2 = Frame(pagec2,bg='white',height=1000,width=700)
framec2_2.pack()

Label(framec2_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35)).place(x=20,y=20)
Label(framec2_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20)).place(x=20,y=80)

Label(framec2_1,text="Roll No: ",bg='black',fg='white',font=("bold",20),justify=LEFT).place(y=0)
Label(framec2_1,text="Rank: ",bg='black',fg='white',font=("bold",20),justify=RIGHT).place(x=450,y=0)

Button(framec2_2, text="<--Back",width=10,bg='brown',fg='white',command=lambda:raise_frame(pagec0)).place(x=5,y=5)

labelframec2_1 = LabelFrame(framec2_2, text="Enter Personal Details",width=600,height=300)
labelframec2_1.place(x=50,y=33)
label_c2_1 = Label(labelframec2_1, text="FullName",width=20,font=("bold", 10))
label_c2_1.place(x=80,y=30)
entry_c2_1 = Entry(labelframec2_1,textvar = name1)
entry_c2_1.place(x=240,y=30)
label_c2_2 = Label(labelframec2_1, text="Email",width=20,font=("bold", 10))
label_c2_2.place(x=68,y=80)
entry_c2_2 = Entry(labelframec2_1,textvar = email1)
entry_c2_2.place(x=240,y=80)
label_c2_3 = Label(labelframec2_1, text="Gender",width=20,font=("bold", 10))
label_c2_3.place(x=70,y=130)
Radiobutton(labelframec2_1, text="Male", variable=gender1, value='Male').place(x=235,y=130)
Radiobutton(labelframec2_1, text="Female", variable=gender1, value='Female').place(x=290,y=130)
label_c2_4 = Label(labelframec2_1, text="State",width=20,font=("bold", 10))
label_c2_4.place(x=65,y=180)
list1 = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']
droplist=OptionMenu(labelframec2_1,state1, *list1)
droplist.config(width=15)
state1.set('Select your State') 
droplist.place(x=240,y=180)
label_c2_5 = Label(labelframec2_1, text="Category",width=20,font=("bold", 10))
label_c2_5.place(x=74,y=230)
Radiobutton(labelframec2_1, text="General", variable=category1, value='General').place(x=235,y=230)
Radiobutton(labelframec2_1, text="OBC", variable=category1, value='OBC').place(x=310,y=230)
Radiobutton(labelframec2_1, text="SC/ST", variable=category1, value='SC/ST').place(x=370,y=230)
labelframec2_2 = LabelFrame(framec2_2, text="Enter Academic Details of class 12th",width=600,height=150)
labelframec2_2.place(x=50,y=350)
label_c2_6 = Label(labelframec2_2, text="Board",width=20,font=("bold", 10))
label_c2_6.place(x=70,y=25)
Radiobutton(labelframec2_2, text="CBSE", variable=board1, value='CBSE').place(x=235,y=25)
Radiobutton(labelframec2_2, text="HBSE", variable=board1, value='HBSE').place(x=300,y=25)
Radiobutton(labelframec2_2, text="MBSE", variable=board1, value='MBSE').place(x=360,y=25)
label_c2_7 = Label(labelframec2_2, text="School Name",width=20,font=("bold", 10))
label_c2_7.place(x=70,y=60)
entry_c2_7 = Entry(labelframec2_2,width=50,textvar=school1)
entry_c2_7.place(x=235,y=60)
label_c2_8 = Label(labelframec2_2, text="Percentage",width=20,font=("bold", 10))
label_c2_8.place(x=70,y=100)
entry_c2_8 = Entry(labelframec2_2,width=10,textvar=percentage1)
entry_c2_8.place(x=235,y=100)
 
Button(framec2_2, text='Next ->',width=20,bg='brown',fg='white',command=database2).place(x=500,y=550)






###################################################PAGEC3

pagec3 = Frame(root,width=700,height=1000,bg='red')
pagec3.grid(row=0,column=0,sticky='news')

varplace=0
indexplace=0
collegelist=[]
college1 = StringVar()

framec3_0 = Frame(pagec3,bg='blue',height=150,width=700)
framec3_0.pack()
framec3_1 = Frame(pagec3,bg='black',height=50,width=700)
framec3_1.pack()
framec3_2 = Frame(pagec3,bg='white',height=850,width=700)
framec3_2.pack()
framec3_3 = Frame(framec3_2,bg='green',height=300,width=500)
framec3_3.place(x=100,y=210)

labelc3_0 = Label(framec3_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35))
labelc3_0.place(x=20,y=20)
labelc3_1 = Label(framec3_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20))
labelc3_1.place(x=20,y=80)

Label(framec3_1,text="Roll No: ",bg='black',fg='white',font=("bold",20),justify=LEFT).place(y=0)
Label(framec3_1,text="Rank: ",bg='black',fg='white',font=("bold",20),justify=RIGHT).place(x=450,y=0)

Button(framec3_2, text="<--Back",width=10,bg='brown',fg='white',command=lambda:raise_frame(pagec2)).place(x=5,y=5)
Button(framec3_2, text="View Seat Matrix",width=20,bg='brown',fg='white',command=lambda:raise_frame(pagec4)).place(x=538,y=5)
Label(framec3_2,text="ADD PREFERENCES IN YOUR PREFERENCE LIST",bg='pink',fg='black',font=("bold",20)).place(x=25,y=60)
conn=sqlite3.connect('database.db')
cursor =conn.execute("SELECT CRANK,COLLEGE,BRANCH,SEATS FROM COLLEGEINFO")
for i in cursor:
    collegelist.append(i)        
labelc3_4 = Label(framec3_2, text="OPTIONS     :",width=36,bg='red',font=("bold", 20),anchor='w')
labelc3_4.place(x=65,y=130)
droplist=OptionMenu(framec3_2,college1,*collegelist)
droplist.config(width=50,bg='black',fg='white')
college1.set('Click to view options') 
droplist.place(x=300,y=134)
Button(framec3_2, text="Add",width=10,bg='brown',fg='white',command=database3).place(x=300,y=180)
Button(framec3_2, text="Final Submit",width=10,bg='brown',fg='white',font=("bold",20),command=box).place(x=270,y=520)






###################################################PAGEC4
pagec4 = Frame(root,width=700,height=1000,bg='red')
pagec4.grid(row=0,column=0,sticky='news')
ind1,ind2=0,0
list1=[5,30,30,5]
list2=['black','red','black','red']
list3=[75,125,325,575]
list4=['CRank','College Name','Branch','Seats']

framec4_0 = Frame(pagec4,bg='blue',height=150,width=700)
framec4_0.pack()
framec4_1 = Frame(pagec4,bg='white',height=850,width=700)
framec4_1.pack()

labelc4_0 = Label(framec4_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35))
labelc4_0.place(x=20,y=20)
labelc4_1 = Label(framec4_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20))
labelc4_1.place(x=20,y=80)


Button(framec4_1, text="<--Back",width=10,bg='brown',fg='white',command=lambda:raise_frame(pagec3)).place(x=5,y=5)
Label(framec4_1,text="JOINT EXAM COLLEGE  SEATS MATRIX",bg='green',fg='yellow',font=("bold",25)).place(x=30,y=60)
conn = sqlite3.connect('database.db')
cursor =conn.execute("SELECT CRANK,COLLEGE,BRANCH,SEATS FROM COLLEGEINFO")
for ind2 in range(0,4):
    Label(framec4_1,text=list4[ind2],bg='pink',fg='black',width=list1[ind2],font="Times,10,bold",anchor='w').place(x=list3[ind2],y=140)
cursor =conn.execute("SELECT CRANK,COLLEGE,BRANCH,SEATS FROM COLLEGEINFO")
for i in cursor:
    ind2=0
    for j in i:
        Label(framec4_1,text=j,bg=list2[ind2],fg='white',width=list1[ind2],font="Times,5,bold",anchor='w').place(x=list3[ind2],y=170+ind1*20)
        ind2+=1
    ind1+=1
conn.commit()
conn.close()





###################################################PAGEC5
pagec5 = Frame(root,width=700,height=1000,bg='red')
pagec5.grid(row=0,column=0,sticky='news')

framec5_0 = Frame(pagec5,bg='blue',height=150,width=700)
framec5_0.pack()
framec5_1 = Frame(pagec5,bg='pink',height=850,width=700)
framec5_1.pack()

labelc5_0 = Label(framec5_0,text="Joint Exam Counselling - 2019",bg='blue',fg='white',font=("bold",35))
labelc5_0.place(x=20,y=20)
labelc5_1 = Label(framec5_0,text="Counselling for admission to IITs, NITs and IIITs for the Academic Year 2019-20",bg='blue',fg='white',font=(20))
labelc5_1.place(x=20,y=80)

Label(framec5_1,text="""---""",bg='pink',fg='white',font=("bold",15),anchor='c').place(x=90,y=150)

Button(framec5_1, text="<--Back",width=10,bg='brown',fg='white',command=lambda:raise_frame(pagec0)).place(x=5,y=5)
Label(framec5_1,text="JOINT EXAM COUNSELLING RESULT",bg='green',fg='yellow',font=("bold",25)).place(x=60,y=60)

raise_frame(home)
root.mainloop()
