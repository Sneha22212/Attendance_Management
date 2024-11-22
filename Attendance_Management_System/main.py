from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
import os
import subprocess

from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help

class Face_recognition_class:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")

        # First image
        img1 = Image.open("bgimages/im1.jpg")
        img1 = img1.resize((250, 150), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  # Convert PIL image to Tkinter PhotoImage
        label_1 = Label(self.root, image=self.photoimg1)
        label_1.place(x=340, y=0, width=250, height=150)

        # Second image
        img2 = Image.open("bgimages/im2.jpg")
        img2 = img2.resize((250, 150), Image.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)  
        label_2 = Label(self.root, image=self.photoimg2)
        label_2.place(x=590, y=0, width=250, height=150)

        # Third image
        img3 = Image.open("bgimages/im3.jpg")
        img3 = img3.resize((280, 150), Image.LANCZOS) 
        self.photoimg3 = ImageTk.PhotoImage(img3)  
        label_3 = Label(self.root, image=self.photoimg3)
        label_3.place(x=840, y=0, width=280, height=150)

        # Background image
        bg = Image.open("bgimages/bg.jpg")
        bg = bg.resize((1550, 750), Image.LANCZOS) 
        self.bgimg = ImageTk.PhotoImage(bg)  
        bg_label = Label(self.root, image=self.bgimg)
        bg_label.place(x=0, y=150, width=1550, height=750)

        # Small image at top-left
        img = Image.open("bgimages/i.jpg")
        img = img.resize((340, 150), Image.LANCZOS) 
        self.bimg = ImageTk.PhotoImage(img)  
        img_label_1 = Label(self.root, image=self.bimg)
        img_label_1.place(x=0, y=0, width=340, height=150)

        # Second small image at top-right
        img4 = Image.open("bgimages/i.jpg")
        img4 = img4.resize((360, 150), Image.LANCZOS) 
        self.b2img = ImageTk.PhotoImage(img4)  
        img_label_2 = Label(self.root, image=self.b2img)
        img_label_2.place(x=1080, y=0, width=370, height=150)

        # Title label
        title_1 = Label(bg_label, text='ATTENDANCE  MANAGEMENT  SYSTEM', font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_1.place(x=0, y=0, width=1430, height=55)

        # Student button 
        img5 = Image.open("frontpage button/student.jpg")
        img5 = img5.resize((350, 200), Image.LANCZOS) 
        self.photoimg4 = ImageTk.PhotoImage(img5)  

        b1 = Button(self.root, image=self.photoimg4,command=self.student_details, cursor="hand")
        b1.place(x=80, y=280, width=350, height=200)

        b1_1 = Button(self.root, text="Student Details",command=self.student_details, cursor="hand", font=("times new roman", 18, "bold"), fg="blue")
        b1_1.place(x=80, y=480, width=352, height=30)  # Consistent height

        # Detect face button 
        img6 = Image.open("frontpage button/facedetector.jpg")
        img6 = img6.resize((350, 200), Image.LANCZOS) 
        self.photoimg5 = ImageTk.PhotoImage(img6)  

        b2 = Button(self.root, image=self.photoimg5, cursor="hand",command=self.face_data)
        b2.place(x=530, y=280, width=350, height=200)

        b2_1 = Button(self.root, text="Face Detector", cursor="hand",command=self.face_data ,font=("times new roman", 18, "bold"), fg="blue")
        b2_1.place(x=530, y=480, width=352, height=30)  # Consistent height

        #Attendance button
        img7 = Image.open("frontpage button/facedetector button.jpg")
        img7 = img7.resize((350, 200), Image.LANCZOS) 
        self.photoimg6 = ImageTk.PhotoImage(img7)  

        b3 = Button(self.root, image=self.photoimg6, cursor="hand",command=self.attendance_data)
        b3.place(x=982, y=280, width=350, height=200)

        b3_1 = Button(self.root, text="Attendance", cursor="hand",command=self.attendance_data ,font=("times new roman", 18, "bold"), fg="blue")
        b3_1.place(x=982, y=480, width=352, height=30)  # Consistent height

        # Help Desk button
        img8 = Image.open("frontpage button/help.jpg")
        img8 = img8.resize((350, 200), Image.LANCZOS) 
        self.photoimg7 = ImageTk.PhotoImage(img8)  

        b4 = Button(self.root, image=self.photoimg7,command=self.help_data ,cursor="hand")
        b4.place(x=80, y=550, width=350, height=200)

        b4_1 = Button(self.root, text="Help Desk",command=self.help_data ,cursor="hand", font=("times new roman", 18, "bold"), fg="blue")
        b4_1.place(x=80, y=750, width=352, height=30)  # Consistent height

        # Train data
        img9 = Image.open("frontpage button/train.jpg")
        img9 = img9.resize((350, 200), Image.LANCZOS) 
        self.photoimg8 = ImageTk.PhotoImage(img9)  

        b5 = Button(self.root, image=self.photoimg8, cursor="hand",command=self.train_data)
        b5.place(x=530, y=550, width=350, height=200)

        b5_1 = Button(self.root, text="Train Data", cursor="hand",command=self.train_data ,font=("times new roman", 18, "bold"), fg="blue")
        b5_1.place(x=530, y=750, width=352, height=30)  # Consistent height

        # Photos
        img10 = Image.open("frontpage button/photos.jpg")
        img10 = img10.resize((350, 200), Image.LANCZOS) 
        self.photoimg9 = ImageTk.PhotoImage(img10)  

        b6 = Button(self.root, image=self.photoimg9, cursor="hand",command=self.open_img)
        b6.place(x=982, y=550, width=350, height=200)

        b6_1 = Button(self.root, text="Photos", cursor="hand",command=self.open_img ,font=("times new roman", 18, "bold"), fg="blue")
        b6_1.place(x=982, y=750, width=352, height=30)  # Consistent height

        # Developer
        # img11 = Image.open("/Attendance_Management_System/frontpage button/developer.jpg")
        # img11 = img11.resize((250, 150), Image.LANCZOS) 
        # self.photoimg10 = ImageTk.PhotoImage(img11)  

        # b7 = Button(self.root, image=self.photoimg10, cursor="hand")
        # b7.place(x=730, y=550, width=250, height=150)

        # b7_1 = Button(self.root, text="Developer", cursor="hand", font=("times new roman", 18, "bold"), fg="blue")
        # b7_1.place(x=730, y=700, width=250, height=30)  # Consistent height

        # Exit
        img12 = Image.open("frontpage button/exit.jpg")
        img12 = img12.resize((100, 40), Image.LANCZOS) 
        self.photoimg11 = ImageTk.PhotoImage(img12)  

        b8 = Button(self.root, image=self.photoimg11,command=self.iExit ,cursor="hand")
        b8.place(x=1320, y=840, width=100, height=40)

        # b8_1 = Button(self.root, text="Exit", cursor="hand", font=("times new roman", 18, "bold"), fg="blue")
        # b8_1.place(x=1100, y=880, width=210, height=22)  # Consistent height




    def open_img(self):
        subprocess.call(["open", "data"])




    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


# Main driver code
if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_class(root)
    root.mainloop()
