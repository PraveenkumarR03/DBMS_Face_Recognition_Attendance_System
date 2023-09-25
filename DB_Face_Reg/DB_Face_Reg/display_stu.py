import tkinter as tk
import tkinter.font as tkFont

import getpass
import mysql.connector

def db(reg):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user='root',
        password='Praveen12#',
        database="student"
        )
    print(mydb)
    mycursor = mydb.cursor() 

    

    q="select Reg_no,stu_name,dept,dob,stu_year,start_year,phone_no,address,attend from stu_details where Reg_no = "+str(reg)+""
    mycursor.execute(q)
    result=mycursor.fetchall()

    q1="select Reg_no,cgpa from results where Reg_no = "+str(reg)+""
    mycursor.execute(q1)
    result1=mycursor.fetchall()
    

    q2="select c_id,c_name,handle,credits from course where c_id = (select c_id from Student where Reg_no = "+str(reg)+")"
    mycursor.execute(q2)
    result2=mycursor.fetchall()

    print("re :{} \n re1 :{} \n re2:{}".format(result,result1,result2))
    return result,result1,result2,mydb.commit()

class Display:
    def __init__(self, root, id):
        #setting title
        root.title("Display")
        #setting window size
        width=640
        height=480
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        r,r1,r2,f=db(id)
        r,r1,r2=str(r),str(r1),str(r2)
        r=r.replace("[(","")
        r=r.replace(")]","")
        r1=r1.replace("[(","")
        r1=r1.replace(")]","")
        r2=r2.replace("[(","")
        r2=r2.replace(")]","")
        r,r1,r2=list(r.replace("'","").split(",")),list(r1.replace("'","").split(",")),list(r2.replace("'","").split(","))
        
        GMessage_202=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_202["font"] = ft
        GMessage_202["fg"] = "#333333"
        GMessage_202["justify"] = "center"
        GMessage_202["text"] = "Name"
        GMessage_202.place(x=40,y=70,width=80,height=25)

        GMessage_462=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_462["font"] = ft
        GMessage_462["fg"] = "#333333"
        GMessage_462["justify"] = "center"
        GMessage_462["text"] = "Department"
        GMessage_462.place(x=40,y=120,width=80,height=25)

        GMessage_751=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_751["font"] = ft
        GMessage_751["fg"] = "#333333"
        GMessage_751["justify"] = "center"
        GMessage_751["text"] = "Start Year"
        GMessage_751.place(x=40,y=170,width=80,height=25)

        GMessage_970=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_970["font"] = ft
        GMessage_970["fg"] = "#333333"
        GMessage_970["justify"] = "center"
        GMessage_970["text"] = "Current Year"
        GMessage_970.place(x=40,y=220,width=80,height=25)

        GMessage_351=tk.Message(root)
        ft = tkFont.Font(family='Times',size=8)
        GMessage_351["font"] = ft
        GMessage_351["fg"] = "#333333"
        GMessage_351["justify"] = "center"
        GMessage_351["text"] = "Roll No"
        GMessage_351.place(x=40,y=30,width=80,height=25)

        GMessage_699=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_699["font"] = ft
        GMessage_699["fg"] = "#333333"
        GMessage_699["justify"] = "center"
        GMessage_699["text"] = "DOB"
        GMessage_699.place(x=300,y=20,width=80,height=25)

        GMessage_369=tk.Message(root)
        ft = tkFont.Font(family='Times',size=8)
        GMessage_369["font"] = ft
        GMessage_369["fg"] = "#333333"
        GMessage_369["justify"] = "center"
        GMessage_369["text"] = "Address"
        GMessage_369.place(x=300,y=120,width=90,height=25)

        GMessage_940=tk.Message(root)
        ft = tkFont.Font(family='Times',size=8)
        GMessage_940["font"] = ft
        GMessage_940["fg"] = "#333333"
        GMessage_940["justify"] = "center"
        GMessage_940["text"] = "Phone No"
        GMessage_940.place(x=300,y=70,width=80,height=25)

        GMessage_300=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_300["font"] = ft
        GMessage_300["fg"] = "#333333"
        GMessage_300["justify"] = "center"
        GMessage_300["text"] = "CGPA"
        GMessage_300.place(x=300,y=210,width=80,height=25)

        GLabel_732=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_732["font"] = ft
        GLabel_732["fg"] = "#333333"
        GLabel_732["justify"] = "center"
        GLabel_732["text"] = "STUDENT :"
        GLabel_732.place(x=0,y=0,width=79,height=30)

        GLabel_145=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
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

        GMessage_59=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_59["font"] = ft
        GMessage_59["fg"] = "#333333"
        GMessage_59["justify"] = "center"
        GMessage_59["text"] = "Course Name"
        GMessage_59.place(x=300,y=290,width=80,height=25)

        GMessage_161=tk.Message(root)
        ft = tkFont.Font(family='Times',size=8)
        GMessage_161["font"] = ft
        GMessage_161["fg"] = "#333333"
        GMessage_161["justify"] = "center"
        GMessage_161["text"] = "Handle By"
        GMessage_161.place(x=40,y=340,width=80,height=25)

        GMessage_928=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_928["font"] = ft
        GMessage_928["fg"] = "#333333"
        GMessage_928["justify"] = "center"
        GMessage_928["text"] = "Credits"
        GMessage_928.place(x=300,y=340,width=80,height=25)

        GLabel_693=tk.Label(root)
        GLabel_693["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_693["font"] = ft
        GLabel_693["fg"] = "#333333"
        GLabel_693["justify"] = "center"
        GLabel_693["text"] = r[0]
        GLabel_693.place(x=150,y=30,width=100,height=25)

        GLabel_617=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_617["font"] = ft
        GLabel_617["fg"] = "#333333"
        GLabel_617["justify"] = "center"
        GLabel_617["text"] = r[1]
        GLabel_617.place(x=150,y=70,width=100,height=25)

        GLabel_861=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#333333"
        GLabel_861["justify"] = "center"
        GLabel_861["text"] = r[2]
        GLabel_861.place(x=150,y=120,width=100,height=25)

        GLabel_748=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_748["font"] = ft
        GLabel_748["fg"] = "#333333"
        GLabel_748["justify"] = "center"
        GLabel_748["text"] = r[4]
        GLabel_748.place(x=150,y=170,width=100,height=25)

        GLabel_154=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["justify"] = "center"
        GLabel_154["text"] = r[3]
        GLabel_154.place(x=150,y=220,width=100,height=25)

        GLabel_380=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_380["font"] = ft
        GLabel_380["fg"] = "#333333"
        GLabel_380["justify"] = "center"
        GLabel_380["text"] = r[5]
        GLabel_380.place(x=430,y=20,width=100,height=25)

        GLabel_545=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_545["font"] = ft
        GLabel_545["fg"] = "#333333"
        GLabel_545["justify"] = "center"
        GLabel_545["text"] = r[6]
        GLabel_545.place(x=430,y=70,width=100,height=25)

        GLabel_94=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_94["font"] = ft
        GLabel_94["fg"] = "#333333"
        GLabel_94["justify"] = "center"
        GLabel_94["text"] = r[7]
        GLabel_94.place(x=430,y=120,width=165,height=65)

        GLabel_222=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_222["font"] = ft
        GLabel_222["fg"] = "#333333"
        GLabel_222["justify"] = "center"
        GLabel_222["text"] = r1[1]
        GLabel_222.place(x=430,y=210,width=100,height=25)

        GLabel_915=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_915["font"] = ft
        GLabel_915["fg"] = "#333333"
        GLabel_915["justify"] = "center"
        GLabel_915["text"] = r2[0]
        GLabel_915.place(x=150,y=290,width=100,height=25)

        GLabel_879=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_879["font"] = ft
        GLabel_879["fg"] = "#333333"
        GLabel_879["justify"] = "center"
        GLabel_879["text"] = r2[1]
        GLabel_879.place(x=430,y=290,width=100,height=25)

        GLabel_877=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_877["font"] = ft
        GLabel_877["fg"] = "#333333"
        GLabel_877["justify"] = "center"
        GLabel_877["text"] = r2[2]
        GLabel_877.place(x=150,y=340,width=100,height=25)

        GLabel_397=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_397["font"] = ft
        GLabel_397["fg"] = "#333333"
        GLabel_397["justify"] = "center"
        GLabel_397["text"] = r2[3]
        GLabel_397.place(x=430,y=340,width=100,height=25)

        GLabel_566=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_566["font"] = ft
        GLabel_566["fg"] = "#333333"
        GLabel_566["justify"] = "center"
        GLabel_566["text"] = "Press X to Exit"
        GLabel_566.place(x=160,y=440,width=255,height=30)

        GLabel_746=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_746["font"] = ft
        GLabel_746["fg"] = "#333333"
        GLabel_746["justify"] = "center"
        GLabel_746["text"] = "Attendance"
        GLabel_746.place(x=190,y=400,width=70,height=25)

        GLabel_642=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_642["font"] = ft
        GLabel_642["fg"] = "#333333"
        GLabel_642["justify"] = "center"
        GLabel_642["text"] = r[8]
        GLabel_642.place(x=310,y=400,width=70,height=25)
        

if __name__ == "__main__":
    root1 = tk.Tk()
    app1 = Display(root1,485)
    root1.mainloop()
