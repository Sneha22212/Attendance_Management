from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")

        title_1 = Label(self.root, text='HELP DESK', font=("times new roman", 35, "bold"), bg="white", fg="navy")
        title_1.place(x=0, y=0, width=1440, height=65)


        # bg image
        bgmg = Image.open("bgimages/developer.jpg")
        bgmg = bgmg.resize((1550, 900), Image.LANCZOS) 
        self.bgimg = ImageTk.PhotoImage(bgmg)  
        bg_label = Label(self.root, image=self.bgimg)
        bg_label.place(x=0, y=65, width=1550, height=900)

        #title label
        title_1 = Label(bg_label, text='Email: jainsneha42129@gmail.com', font=("times new roman", 30, "bold"), bg="beige", fg="red")
        title_1.place(x=520, y=320, width=480, height=65)

        #title label
        title_1 = Label(bg_label, text='Conatct no: 111 222 333', font=("times new roman", 30, "bold"), bg="beige", fg="red")
        title_1.place(x=520, y=400, width=350, height=65)

        



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
