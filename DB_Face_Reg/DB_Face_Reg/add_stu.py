

from datetime import datetime
from logging import root
import tkinter as tk
import tkinter.font as tkFont
import cv2

import getpass
import mysql.connector

int = 0
def end(int):
    if int == 1:
        return 0
    return 1

def cam(roll_no):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename=r'C:/Users/prave/source/repos/DB_Face_Reg/DB_Face_Reg/Images/'+roll_no+'.png', img=frame)
                webcam.release()
                img_new = cv2.imread(r'C:/Users/prave/source/repos/DB_Face_Reg/DB_Face_Reg/Images/'+roll_no+'.png', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
        
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break    


class App:
    def __init__(self, root):
        #setting title
        root.title("Add Student")
        #setting window size
        width=640
        height=480
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_202=tk.Message(root)
        ft = tkFont.Font(family='Times',size=8)
        GMessage_202["font"] = ft
        GMessage_202["fg"] = "#333333"
        GMessage_202["justify"] = "center"
        GMessage_202["text"] = "Name"
        GMessage_202.place(x=40,y=70,width=80,height=25)

        s_name=tk.Entry(root)
        s_name["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        s_name["font"] = ft
        s_name["fg"] = "#333333"
        s_name["justify"] = "center"
        s_name["text"] = ""
        s_name.place(x=140,y=70,width=100,height=25)

        GMessage_462=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_462["font"] = ft
        GMessage_462["fg"] = "#333333"
        GMessage_462["justify"] = "center"
        GMessage_462["text"] = "Dept"
        GMessage_462.place(x=40,y=120,width=80,height=25)

        GMessage_751=tk.Message(root)
        ft = tkFont.Font(family='Times',size=8)
        GMessage_751["font"] = ft
        GMessage_751["fg"] = "#333333"
        GMessage_751["justify"] = "center"
        GMessage_751["text"] = "Start Year"
        GMessage_751.place(x=40,y=170,width=80,height=25)

        GMessage_970=tk.Message(root)
        ft = tkFont.Font(family='Times',size=8)
        GMessage_970["font"] = ft
        GMessage_970["fg"] = "#333333"
        GMessage_970["justify"] = "center"
        GMessage_970["text"] = "Current Year"
        GMessage_970.place(x=40,y=220,width=80,height=25)

        GMessage_351=tk.Message(root)
        ft = tkFont.Font(family='Times',size=9)
        GMessage_351["font"] = ft
        GMessage_351["fg"] = "#333333"
        GMessage_351["justify"] = "center"
        GMessage_351["text"] = "Roll No"
        GMessage_351.place(x=40,y=20,width=80,height=25)

        r_no=tk.Entry(root)
        r_no["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        r_no["font"] = ft
        r_no["fg"] = "#333333"
        r_no["justify"] = "center"
        r_no["text"] = ""
        r_no.place(x=140,y=20,width=100,height=25)



        s_dep=tk.Entry(root)
        s_dep["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        s_dep["font"] = ft
        s_dep["fg"] = "#333333"
        s_dep["justify"] = "center"
        s_dep["text"] = ""
        s_dep.place(x=140,y=120,width=100,height=25)


        s_syear=tk.Entry(root)
        s_syear["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        s_syear["font"] = ft
        s_syear["fg"] = "#333333"
        s_syear["justify"] = "center"
        s_syear["text"] = ""
        s_syear.place(x=140,y=170,width=100,height=25)


        s_cyear=tk.Entry(root)
        s_cyear["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        s_cyear["font"] = ft
        s_cyear["fg"] = "#333333"
        s_cyear["justify"] = "center"
        s_cyear["text"] = ""
        s_cyear.place(x=140,y=220,width=100,height=25)

        
        GMessage_699=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_699["font"] = ft
        GMessage_699["fg"] = "#333333"
        GMessage_699["justify"] = "center"
        GMessage_699["text"] = "DOB"
        GMessage_699.place(x=300,y=20,width=80,height=25)

        GMessage_369=tk.Message(root)
        ft = tkFont.Font(family='Times',size=7)
        GMessage_369["font"] = ft
        GMessage_369["fg"] = "#333333"
        GMessage_369["justify"] = "center"
        GMessage_369["text"] = "Address"
        GMessage_369.place(x=300,y=120,width=100,height=25)

        dob=tk.Entry(root)
        dob["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        dob["font"] = ft
        dob["fg"] = "#333333"
        dob["justify"] = "center"
        dob["text"] = ""
        dob.place(x=410,y=20,width=100,height=25)

        addr=tk.Entry(root)
        addr["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        addr["font"] = ft
        addr["fg"] = "#333333"
        addr["justify"] = "center"
        addr["text"] = ""
        addr.place(x=410,y=120,width=175,height=65)

        GMessage_940=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_940["font"] = ft
        GMessage_940["fg"] = "#333333"
        GMessage_940["justify"] = "center"
        GMessage_940["text"] = "Phone No"
        GMessage_940.place(x=300,y=70,width=80,height=25)

        p_no=tk.Entry(root)
        p_no["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        p_no["font"] = ft
        p_no["fg"] = "#333333"
        p_no["justify"] = "center"
        p_no["text"] = ""
        p_no.place(x=410,y=70,width=100,height=25)

        GMessage_300=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_300["font"] = ft
        GMessage_300["fg"] = "#333333"
        GMessage_300["justify"] = "center"
        GMessage_300["text"] = "CGPA"
        GMessage_300.place(x=300,y=210,width=80,height=25)

        cgpa=tk.Entry(root)
        cgpa["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        cgpa["font"] = ft
        cgpa["fg"] = "#333333"
        cgpa["justify"] = "center"
        cgpa["text"] = ""
        cgpa.place(x=410,y=210,width=100,height=25)

        GLabel_732=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        GLabel_732["font"] = ft
        GLabel_732["fg"] = "#333333"
        GLabel_732["justify"] = "center"
        GLabel_732["text"] = "STUDENT :"
        GLabel_732.place(x=0,y=0,width=79,height=30)

        GLabel_145=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        GLabel_145["font"] = ft
        GLabel_145["fg"] = "#333333"
        GLabel_145["justify"] = "center"
        GLabel_145["text"] = "COURSE :"
        GLabel_145.place(x=0,y=260,width=70,height=25)

        GMessage_76=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_76["font"] = ft
        GMessage_76["fg"] = "#333333"
        GMessage_76["justify"] = "center"
        GMessage_76["text"] = "Course id"
        GMessage_76.place(x=40,y=290,width=80,height=25)

        c_id=tk.Entry(root)
        c_id["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        c_id["font"] = ft
        c_id["fg"] = "#333333"
        c_id["justify"] = "center"
        c_id["text"] = ""
        c_id.place(x=140,y=290,width=100,height=25)

        GMessage_59=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_59["font"] = ft
        GMessage_59["fg"] = "#333333"
        GMessage_59["justify"] = "center"
        GMessage_59["text"] = "Course Name"
        GMessage_59.place(x=300,y=290,width=80,height=25)

        c_name=tk.Entry(root)
        c_name["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        c_name["font"] = ft
        c_name["fg"] = "#333333"
        c_name["justify"] = "center"
        c_name["text"] = ""
        c_name.place(x=410,y=290,width=100,height=25)

        GMessage_161=tk.Message(root)
        ft = tkFont.Font(family='Times',size=7)
        GMessage_161["font"] = ft
        GMessage_161["fg"] = "#333333"
        GMessage_161["justify"] = "center"
        GMessage_161["text"] = "Handled by"
        GMessage_161.place(x=40,y=340,width=80,height=25)

        c_faculty=tk.Entry(root)
        c_faculty["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        c_faculty["font"] = ft
        c_faculty["fg"] = "#333333"
        c_faculty["justify"] = "center"
        c_faculty["text"] = ""
        c_faculty.place(x=140,y=340,width=100,height=25)

        GMessage_928=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_928["font"] = ft
        GMessage_928["fg"] = "#333333"
        GMessage_928["justify"] = "center"
        GMessage_928["text"] = "Credits"
        GMessage_928.place(x=300,y=340,width=80,height=25)

        c_cre=tk.Entry(root)
        c_cre["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        c_cre["font"] = ft
        c_cre["fg"] = "#333333"
        c_cre["justify"] = "center"
        c_cre["text"] = ""
        c_cre.place(x=410,y=340,width=100,height=25)


        GButton_548=tk.Button(root)
        GButton_548["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_548["font"] = ft
        GButton_548["fg"] = "#000000"
        GButton_548["justify"] = "center"
        GButton_548["text"] = "Take Photo"
        GButton_548.place(x=190,y=410,width=70,height=25)
        GButton_548["command"] = lambda: self.GButton_548_command(r_no.get())


        GButton_127=tk.Button(root)
        GButton_127["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_127["font"] = ft
        GButton_127["fg"] = "#000000"
        GButton_127["justify"] = "center"
        GButton_127["text"] = "Submit"
        GButton_127.place(x=330,y=410,width=70,height=25)
        GButton_127["command"] = lambda: self.GButton_127_command(r_no.get(),s_name.get(),s_dep.get(),s_syear.get(),s_cyear.get(),
                                                                  dob.get(),addr.get(),p_no.get(),cgpa.get(),c_id.get(),c_name.get(),c_faculty.get(),c_cre.get())

        

    def GButton_548_command(self,roll_no):
        cam(roll_no)

    def GButton_127_command(self,roll_no,sname,dept,start_y,curr_y,dob,addr,p_no,cgpa,c_id,c_name,c_faculty,c_cre):
        
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user='root',
        password='Praveen12#',
        database="student"
        )

        print(mydb)
        mycursor = mydb.cursor()

        q="insert into stu_details values( '{}','{}', '{}', '{}', '{}','{}','{}','{}','{}','{}' )".format(roll_no,sname,dept,dob,curr_y,start_y,p_no,addr,"1",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        mycursor.execute(q)

        q1="insert into results values('{}','{}')".format(roll_no,cgpa)
        mycursor.execute(q1)

        q2="insert into course values('{}','{}','{}','{}')".format(c_id,c_name,c_faculty,c_cre)
        mycursor.execute(q2)

        q3="insert into Student values('{}','{}')".format(roll_no,c_id)
        mycursor.execute(q3)

        mydb.commit()
        end(1)





