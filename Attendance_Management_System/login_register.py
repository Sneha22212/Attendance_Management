from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

import os
import subprocess
from main import Face_recognition_class

from student import Student
from train import Train
from attendance import Attendance
from help import Help
import tkinter


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1445x900+0+0")

        bg = Image.open("bgimages/att_bg.jpg")
        bg = bg.resize((1550, 900), Image.LANCZOS) 
        self.bgimg = ImageTk.PhotoImage(bg)  
        bg_label = Label(self.root, image=self.bgimg)
        bg_label.place(x=0, y=0, width=1550, height=900)

        frame=Frame(self.root,bg="black")
        frame.place(x=560,y=170,width=340,height=500)

        img1 = Image.open("bgimages/login.jpg")
        img1 = img1.resize((230, 180), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  
        label_1 = Label(frame, image=self.photoimg1)
        label_1.place(x=50, y=0, width=230, height=180)

        l1=Label(frame,text="Get Started",font=("times new roman",30,"bold"),bg="black",fg="red")
        l1.place(x=50,y=166,width=230,height=50)

        l2=Label(frame,text="Username:",font=("times new roman",25,"bold"),bg="black",fg="white")
        l2.place(x=10,y=224,width=120,height=35)
        self.l2_entry = Entry(frame,width=16, font=("times new roman", 20, "bold"),bg="white",fg="black")
        self.l2_entry.place(x=140,y=224,width=180,height=35)

        l3=Label(frame,text="Password:",font=("times new roman",25,"bold"),bg="black",fg="white")
        l3.place(x=10,y=280,width=120,height=35)
        self.l3_entry = Entry(frame,width=16, font=("times new roman", 20, "bold"),bg="white",fg="black")
        self.l3_entry.place(x=140,y=280,width=180,height=35)

        #login button
        b2=Button(frame,text="Login",font=("times new roman",27,"bold"),bg="white",fg="red",command=self.login)
        b2.place(x=10,y=335,width=320,height=42)

        #forgot password button
        b1=Button(frame,text="Forgot password?",command=self.forgot_password,font=("times new roman",15,"bold"),bg="black",fg="blue")
        b1.place(x=10,y=395,width=135,height=32)


        #register button
        b3=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),bg="black",fg="blue")
        b3.place(x=10,y=435,width=135,height=32)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.l2_entry.get()=="" or self.l3_entry.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.l2_entry.get()=="abcd" and self.l3_entry.get()=="12345678" :
            messagebox.showinfo("Success","Successfully logged in")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sn@221204",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.l2_entry.get(),
                                                                                        self.l3_entry.get()    
                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showinfo("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recognition_class(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()
      

    def reset(self):
        if self.security_combo.get()=="":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.security_entry.get()=="":
            messagebox.showerror("Error","Please enter security answer",parent=self.root2)
        elif self.newpass_entry.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sn@221204",database="project")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.l2_entry.get(),self.security_combo.get(),self.security_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Incorrect answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s ")
                value=(self.newpass_entry.get(),self.l2_entry.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset",parent=self.root2)
                self.root2.destroy()


    def forgot_password(self):
        if self.l2_entry.get()=="":
            messagebox.showerror("Error","Please enter email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sn@221204",database="project")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.l2_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror('Error','Please enter valid username')
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("500x500+610+170")

                lb=Label(self.root2,text="Forgot Password",font=("times new roman",24,"bold"),bg="white",fg="red")
                lb.place(x=0,y=3,relwidth=1)

                security_label=Label(self.root2,text="Select Security Question",font=("times new roman", 26, "bold"),bg="gray",fg="white")
                security_label.place(x=70,y=60,width=350,height=50)
                self.security_combo=ttk.Combobox(self.root2,width=16,font=("times new roman", 20, "bold"),state="readonly")
                self.security_combo["values"]=("Select","Your birth place","Your pet name","Your favourite book")
                self.security_combo.place(x=70,y=110,width=355,height=50)
                self.security_combo.current(0)

                security_ans_label=Label(self.root2,text="Security Answer",font=("times new roman", 26, "bold"),bg="gray",fg="white")
                security_ans_label.place(x=70,y=170,width=350,height=50)
                self.security_entry=Entry(self.root2,width=16,font=("times new roman", 20, "bold"),bg="black",fg="white")
                self.security_entry.place(x=66,y=220,width=352,height=50)

                newpass_label=Label(self.root2,text="New Password",font=("times new roman", 26, "bold"),bg="gray",fg="white")
                newpass_label.place(x=70,y=280,width=350,height=50)
                self.newpass_entry=Entry(self.root2,width=16,font=("times new roman", 20, "bold"),bg="black",fg="white")
                self.newpass_entry.place(x=66,y=330,width=352,height=50)

                btn=Button(self.root2,text="Reset",command=self.reset,font=("times new roman",25,"bold"),fg="green",bg="white")
                btn.place(x=66,y=420,width=200,height=50)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1445x900+0+0")

        #----textvariables-------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sec=StringVar()
        self.var_sec_ans=StringVar()
        self.var_pass=StringVar()
        self.var_confp=StringVar()
        self.var_check=IntVar()


        bg=Image.open("bgimages/register.jpg")
        bg=bg.resize((1550, 900), Image.LANCZOS) 
        self.bgimg = ImageTk.PhotoImage(bg)  
        bg_label = Label(self.root, image=self.bgimg)
        bg_label.place(x=0, y=0, width=1550, height=900)

        frame=Frame(bg_label,bg="white")
        frame.place(x=130,y=150,width=1200,height=600)

        img1=Image.open("bgimages/register_bg.jpg")
        img1=img1.resize((600,600),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        l1=Label(frame,image=self.photoimg1)
        l1.place(x=0,y=0,width=600,height=600)

        l2=Label(frame,text="REGISTER HERE",font=("times new roman",30,"bold"),bg="white",fg="navy")
        l2.place(x=610,y=10,width=320,height=40)

        fname_label=Label(frame,text="First name",font=("times new roman", 18, "bold"),bg="white",fg="black")
        fname_label.place(x=655,y=70,width=100,height=30)
        self.fname_entry=Entry(frame,width=16,textvariable=self.var_fname,font=("times new roman", 16, "bold"),bg="white",fg="black")
        self.fname_entry.place(x=655,y=105,width=200,height=30)

        lname_label=Label(frame,text="Last name",font=("times new roman", 18, "bold"),bg="white",fg="black")
        lname_label.place(x=920,y=70,width=100,height=30)
        self.lname_entry=Entry(frame,width=16,textvariable=self.var_lname,font=("times new roman", 16, "bold"),bg="white",fg="black")
        self.lname_entry.place(x=920,y=105,width=200,height=30)

        contact_label=Label(frame,text="Contact No",font=("times new roman", 18, "bold"),bg="white",fg="black")
        contact_label.place(x=655,y=145,width=100,height=30)
        self.contact_entry=Entry(frame,width=16,textvariable=self.var_contact,font=("times new roman", 16, "bold"),bg="white",fg="black")
        self.contact_entry.place(x=655,y=180,width=200,height=30)

        email_label=Label(frame,text="Email",font=("times new roman", 18, "bold"),bg="white",fg="black")
        email_label.place(x=920,y=145,width=100,height=30)
        self.email_entry=Entry(frame,width=16,textvariable=self.var_email,font=("times new roman", 16, "bold"),bg="white",fg="black")
        self.email_entry.place(x=920,y=180,width=200,height=30)

        security_label=Label(frame,text="Select Security Question",font=("times new roman", 18, "bold"),bg="white",fg="black")
        security_label.place(x=655,y=220,width=200,height=30)
        self.security_combo=ttk.Combobox(frame,width=16,textvariable=self.var_sec,font=("times new roman", 16, "bold"),state="readonly")
        self.security_combo["values"]=("Select","Your birth place","Your pet name","Your favourite book")
        self.security_combo.place(x=655,y=255,width=200,height=30)
        self.security_combo.current(0)

        security_ans_label=Label(frame,text="Security Answer",font=("times new roman", 18, "bold"),bg="white",fg="black")
        security_ans_label.place(x=920,y=220,width=170,height=30)
        self.security_entry=Entry(frame,width=16,textvariable=self.var_sec_ans,font=("times new roman", 16, "bold"),bg="white",fg="black")
        self.security_entry.place(x=920,y=255,width=200,height=30)

        password_label=Label(frame,text="Password",font=("times new roman", 18, "bold"),bg="white",fg="black")
        password_label.place(x=655,y=295,width=100,height=30)
        self.password_entry=Entry(frame,width=16,textvariable=self.var_pass,font=("times new roman", 16, "bold"),bg="white",fg="black")
        self.password_entry.place(x=655,y=330,width=200,height=30)

        confirm_pass_label=Label(frame,text="Confirm Password",font=("times new roman", 18, "bold"),bg="white",fg="black")
        confirm_pass_label.place(x=920,y=295,width=170,height=30)
        self.confirm_pass_entry=Entry(frame,width=16,textvariable=self.var_confp,font=("times new roman", 16, "bold"),bg="white",fg="black")
        self.confirm_pass_entry.place(x=920,y=330,width=200,height=30)

        #----checkbutton-----
        chkb=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",17,"bold"),bg="white",fg="black",onvalue=1,offvalue=0)
        chkb.place(x=655,y=390)

        #-----buttons--------
        # register buttotn
        im_2=Image.open("bgimages/registerbuttton.jpg")
        im_2=im_2.resize((180,60),Image.LANCZOS)
        self.photoim_2=ImageTk.PhotoImage(im_2)
        b=Button(frame,command=self.register_data,image=self.photoim_2,borderwidth=0,cursor="hand2")
        b.place(x=655,y=450,width=180,height=60)

        # login btn
        im_3=Image.open("bgimages/loginbtn.jpg")
        im_3=im_3.resize((180,60),Image.LANCZOS)
        self.photoim_3=ImageTk.PhotoImage(im_3)
        b=Button(frame,command=self.return_login,image=self.photoim_3,borderwidth=0,cursor="hand2")
        b.place(x=920,y=450,width=180,height=60)

    #-----function declaration-------
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sec_ans.get()=="Select" or self.var_pass.get()=="" or self.var_confp.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confp.get():
            messagebox.showerror("Error","Password didnt match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sn@221204",database="project")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already registered ,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_sec.get(),
                                                                                        self.var_sec_ans.get(),
                                                                                        self.var_pass.get()
                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()

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
        self.app=Face_recognition_class(self.new_window)

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







if __name__ == "__main__":
    main()
