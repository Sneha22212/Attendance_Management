from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")

        title_1 = Label(self.root, text='FACE RECOGNITION', font=("times new roman", 35, "bold"), bg="white", fg="navy")
        title_1.place(x=0, y=0, width=1450, height=65)

        # Displaying images on the GUI
        img1 = Image.open("frontpage button/facedetector.jpg")
        img1 = img1.resize((750, 850), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1) 
        label_1 = Label(self.root, image=self.photoimg1)
        label_1.place(x=0, y=66, width=750, height=850)

        img2 = Image.open("frontpage button/facedet1.jpg")
        img2 = img2.resize((750, 850), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2) 
        label_2 = Label(self.root, image=self.photoimg2)
        label_2.place(x=750, y=66, width=750, height=850)

        #button
        b1=Button(label_2,text="Face Recognition",cursor="hand",font=("times new roman",35,"bold"),bg="white",fg="red",border=7,command=self.face_recog)
        b1.place(x=195,y=45,width=350,height=70)

    #-----face recognition function----
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Sn@221204", database="project")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where sid="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where sid="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where sid="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)



                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
