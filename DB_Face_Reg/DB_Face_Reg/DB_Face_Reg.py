import os
import numpy as np
import cv2
import face_recognition
import cvzone
import pickle
import tkinter as tk
import getpass
import mysql.connector
from datetime import datetime

from add_stu import App
from display_stu import Display


def dtset(reg,att):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user='root',
        password='Praveen12#',
        database="student"
        )
    print(mydb)
    mycursor = mydb.cursor()

    q="update stu_details set attend = "+str(att)+" where Reg_no = "+str(reg)+""

    mycursor.execute(q)
    mydb.commit()

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
    
    res= mycursor.fetchall()
    return res,mydb.commit()

def dt(reg):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user='root',
        password='Praveen12#',
        database="student"
        )
    print(mydb)
    mycursor = mydb.cursor()

    q="select dt from stu_details where Reg_no = "+str(reg)+""

    mycursor.execute(q)
    
    res= mycursor.fetchall()
    return res,mydb.commit()


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread(r'C:\Users\prave\source\repos\DB_Face_Reg\DB_Face_Reg\background.png')


exec(open(r'C:\Users\prave\source\repos\DB_Face_Reg\DB_Face_Reg\EncodeGenerator.py').read())
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []


while True:
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    
    imgBackground[162:162 + 480, 55:55 + 640] = img
    

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("matches", matches)
            # print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)
            # print("Match Index", matchIndex)

            if matches[matchIndex]:
                # print("Known Face Detected")
                print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                if(studentIds[matchIndex]=="321654"):
                    cv2.destroyAllWindows()
                    if __name__ == "__main__":
                        root = tk.Tk()
                        app = App(root)
                        root.mainloop()
                else:
                    
                    id = studentIds[matchIndex]
        
                    d,f=dt(studentIds[matchIndex])
                    dti,f=db(studentIds[matchIndex])
                    dti=str(dti)
                    dti=dti.replace("[(","")
                    dti=dti.replace(")]","")
                    dti=list(dti.replace("'","").split(","))
                    print(d[0][0])
                    datetimeObject = d[0][0]
                    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                    print("timmeeee",secondsElapsed)
                    if secondsElapsed > 30:
                        dtset(id,int(dti[8])+1)

                    if __name__ == "__main__":
                        root1 = tk.Tk()
                        app1 = Display(root1,int(studentIds[matchIndex]))
                        root1.mainloop()

            else:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)


                                                                        
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

                    
