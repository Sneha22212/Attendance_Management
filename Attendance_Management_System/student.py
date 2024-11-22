from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")


        #variables----
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       


        # Main frame
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=0, y=0, width=1550, height=900)

        # Background image
        bg = Image.open("student details/bg.jpg")
        bg = bg.resize((1550, 900), Image.LANCZOS) 
        self.bgimg = ImageTk.PhotoImage(bg)  
        bg_label = Label(main_frame, image=self.bgimg)
        bg_label.place(x=0, y=0, width=1550, height=900)

        # Title label on top of the background image
        title_1 = Label(main_frame, text='STUDENT  MANAGEMENT  SYSTEM', font=("times new roman", 35, "bold"), bg="beige", fg="red")
        title_1.place(x=0, y=0, width=1430, height=65)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        left_frame.place(x=60, y=100, width=650, height=750)

        # Inner Label Frame inside Left Label Frame with a title
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 15, "bold"), bg="white", fg="black")
        current_course_frame.place(x=7, y=50, width=620, height=130)
 
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman", 18, "bold"),bg="white",fg="black")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 18, "bold"),width=17,state="read only")
        dep_combo['values']=("Select Department","AIML","CSE","IT","ECE","MAE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman", 18, "bold"),bg="white",fg="black")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 18, "bold"),width=17,state="read only")
        course_combo['values']=("Select Course","SE","BE","TE","FE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)

         #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman", 18, "bold"),bg="white",fg="black")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 18, "bold"),width=17,state="read only")
        year_combo['values']=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)

        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman", 18, "bold"),bg="white",fg="black")
        Semester_label.grid(row=1,column=2,padx=10)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 18, "bold"),width=17,state="read only")
        Semester_combo['values']=("Select Semester","1","2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)

        #Class student Information
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 15, "bold"), bg="white",fg="black")
        class_student_frame.place(x=7, y=220, width=620, height=500)

        #Student Id
        sid_label=Label(class_student_frame,text="StudentID:",font=("times new roman", 18, "bold"),bg="white",fg="black")
        sid_label.grid(row=0,column=0,padx=10,pady=10)
        sid_entry=Entry(class_student_frame,textvariable=self.var_std_id,width=16,font=("times new roman", 14, "bold"))
        sid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        sname_label=Label(class_student_frame,text="Student Name:",font=("times new roman", 18, "bold"),bg="white",fg="black")
        sname_label.grid(row=0,column=2,padx=10,pady=10)
        sname_entry=Entry(class_student_frame,textvariable=self.var_name,width=16,font=("times new roman", 14, "bold"))
        sname_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        class_div_label.grid(row=1, column=0, padx=5, pady=10)

        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman", 18, "bold"),width=10,state="read only")
        division_combo['values']=("A","B","C")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    

        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        roll_no_label.grid(row=1, column=2, padx=5, pady=10)
        roll_no_entry = Entry(class_student_frame, textvariable=self.var_roll,width=16, font=("times new roman", 14, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        #gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        gender_label.grid(row=2, column=0, padx=5, pady=10)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman", 18, "bold"),width=10,state="read only")
        gender_combo['values']=("Female","Male","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #dob
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        dob_label.grid(row=2, column=2, padx=5, pady=10)
        dob_entry = Entry(class_student_frame, textvariable=self.var_dob,width=16, font=("times new roman", 14, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        email_label.grid(row=3, column=0, padx=5, pady=10)
        email_entry = Entry(class_student_frame, textvariable=self.var_email,width=16, font=("times new roman", 14, "bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        phone_label.grid(row=3, column=2, padx=5, pady=10)
        phone_entry = Entry(class_student_frame, textvariable=self.var_phone,width=16, font=("times new roman", 14, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        address_label.grid(row=4, column=0, padx=5, pady=10)
        address_entry = Entry(class_student_frame,textvariable=self.var_address,width=16, font=("times new roman", 14, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher's Name
        teacher_label = Label(class_student_frame, text="Teacher's Name:", font=("times new roman", 18, "bold"), bg="white", fg="black")
        teacher_label.grid(row=4, column=2, padx=5, pady=10)
        teacher_entry = Entry(class_student_frame,textvariable=self.var_teacher ,width=16, font=("times new roman", 14, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        #Radio buttons
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radio1.grid(row=6,column=0,pady=20,padx=15)

        radio2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="no")
        radio2.grid(row=6,column=1,pady=20,padx=15)

        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="lightgray",padx=20)
        btn_frame.place(x=2,y=280,width=900,height=80)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0,padx=5,pady=20)

         #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        update_btn.grid(row=0,column=1,padx=5,pady=20)

         #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        delete_btn.grid(row=0,column=2,padx=5,pady=20)

         #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        reset_btn.grid(row=0,column=3,padx=5,pady=20)

        #button frame 2
        btn_frame2=Frame(class_student_frame,bd=2,relief=RIDGE,bg="lightgray",padx=20)
        btn_frame2.place(x=2,y=360,width=900,height=80)

        take_photo_btn=Button(btn_frame2,text="Take Photo Sample",command=self.generate_dataset,width=25,font=("times new roman",16,"bold"),bg="white",fg="black")
        take_photo_btn.grid(row=0,column=0,padx=20,pady=20)

        update_photo_btn=Button(btn_frame2,text="Update Photo Sample",width=25,font=("times new roman",16,"bold"),bg="white",fg="black")
        update_photo_btn.grid(row=0,column=1,padx=15,pady=20)


        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, width=70,relief=RIDGE, text="Student Details", font=("times new roman", 20, "bold"), bg="white",fg="black")
        right_frame.place(x=740, y=100, width=650, height=750)

        search_frame=LabelFrame(right_frame,bd=2,bg="white",fg="black",relief=RIDGE,text="Search System",font=("times new roman", 15, "bold"))
        search_frame.place(x=7,y=50,width=620,height=100)

        search_label = Label(search_frame, text="Search by:", font=("times new roman", 18, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman", 18, "bold"),width=10,state="read only")
        search_combo['values']=("Select ","Roll no","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",16,"bold"))
        search_entry.grid(row=0,column=2,padx=15)

        search_btn=Button(search_frame,text="Search",width=8,font=("times new roman",16,"bold"),bg="white",fg="black")
        search_btn.grid(row=0,column=3,padx=7,pady=20)

        showAll_btn=Button(search_frame,text="Show All",width=8,font=("times new roman",16,"bold"),bg="white",fg="black")
        showAll_btn.grid(row=0,column=4,pady=20)

        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=170,width=620,height=530)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","sid","name","divi","roll","gender","dob","email","phone","address","teacher","photoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.column("#0", width=0, stretch=NO)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("sid", text="StudentId")  
        self.student_table.heading("name", text="Name")  
        self.student_table.heading("divi", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photoSample", text="Photo Sample") 
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sn@221204",database="project")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            
            except Exception as e:
                messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)

    # ----fetch data-----
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sn@221204",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #---get cursor----
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sn@221204",database="project")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,divi=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where sid=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                 ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}")

    #---delete function----
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Details","Do you want to delete this student ",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sn@221204",database="project")
                    my_cursor=conn.cursor()
                    sql="delete from student where sid=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Details Successfully Deleted",parent=self.root)
            
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}")

    #---reset function----
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_name.set(""),
        self.var_div.set("A"),
        self.var_roll.set(""),
        self.var_gender.set("Female"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #----take photo samples or generate data set-----
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="Sn@221204", database="project")
                my_cursor = conn.cursor()

                # Get the last student id
                my_cursor.execute("SELECT * FROM student")
                my_result = my_cursor.fetchall()
                id = 0

                for x in my_result:
                    id+=1
    
                # # Update student details
                my_cursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, divi=%s, roll=%s,gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photoSample=%s WHERE sid=%s", (
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data for face detection
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 2,7)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None  # Return None if no face is detected

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)  #
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 300:  # Press Enter to stop or capture 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed successfully")

            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
