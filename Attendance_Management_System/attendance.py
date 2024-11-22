from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")

        #--------variables--------
        self.var_attId=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()


        # Main frame
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=0, y=0, width=1550, height=900)

        # Background image
        bg = Image.open("bgimages/att_bg.jpg")
        bg = bg.resize((1550, 900), Image.LANCZOS) 
        self.bgimg = ImageTk.PhotoImage(bg)  
        bg_label = Label(main_frame, image=self.bgimg)
        bg_label.place(x=0, y=0, width=1550, height=900)

         # Title label on top of the background image
        title_1 = Label(main_frame, text='ATTENDANCE  MANAGEMENT  SYSTEM', font=("times new roman", 35, "bold"), bg="navy", fg="white")
        title_1.place(x=0, y=0, width=1450, height=65)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=("times new roman", 20, "bold"), fg="blue", bg="lightgray")
        left_frame.place(x=60, y=100, width=650, height=750)

        #image on left frame
        img=Image.open("bgimages/att2.jpg")
        img=img.resize((650,300),Image.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img)
        img_label=Label(left_frame,image=self.img1) 
        img_label.place(x=0,y=0,width=650,height=220)

        left_inside_frame = LabelFrame(left_frame, bd=2, relief=RIDGE,bg="white")
        left_inside_frame.place(x=7, y=280, width=620, height=400)

        # Attendance Id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman", 22, "bold"),bg="white",fg="black")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10)
        attendanceId_entry=Entry(left_inside_frame,width=16,textvariable=self.var_attId,font=("times new roman", 14, "bold"))
        attendanceId_entry.grid(row=0,column=1,pady=10,sticky=W)

        # Roll No
        roll_no_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 22, "bold"), bg="white", fg="black")
        roll_no_label.grid(row=0, column=2, pady=10)
        roll_no_entry = Entry(left_inside_frame,textvariable=self.var_roll,width=16, font=("times new roman", 14, "bold"))
        roll_no_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        #Student name
        sname_label=Label(left_inside_frame,text="Student Name:",font=("times new roman", 22, "bold"),bg="white",fg="black")
        sname_label.grid(row=1,column=0,padx=10,pady=10)
        sname_entry=Entry(left_inside_frame,textvariable=self.var_name,width=16,font=("times new roman", 14, "bold"))
        sname_entry.grid(row=1,column=1,pady=10,sticky=W)

         #Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman", 22, "bold"),bg="white",fg="black")
        dep_label.grid(row=1,column=2)
        dep_entry=Entry(left_inside_frame,textvariable=self.var_dep,width=16,font=("times new roman", 14, "bold"))
        dep_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        #Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman", 22, "bold"),bg="white",fg="black")
        time_label.grid(row=2,column=0,padx=5,pady=10)
        time_entry=Entry(left_inside_frame,textvariable=self.var_time,width=16,font=("times new roman", 14, "bold"))
        time_entry.grid(row=2,column=1,pady=10,sticky=W)

         #Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman", 22, "bold"),bg="white",fg="black")
        date_label.grid(row=2,column=2)
        date_entry=Entry(left_inside_frame,textvariable=self.var_date,width=16,font=("times new roman", 14, "bold"))
        date_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)

        #Attendance Status
        attendance_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman", 22, "bold"),bg="white",fg="black")
        attendance_label.grid(row=3,column=0,padx=10)

        self.attendance_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attendance,font=("times new roman", 22, "bold"),width=10,state="read only")
        self.attendance_combo['values']=("Status","P","A")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=3,column=1,padx=3,pady=10,sticky=W)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="lightgray",padx=20)
        btn_frame.place(x=2,y=260,width=900,height=80)

        #Import csv button
        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        import_btn.grid(row=0,column=0,padx=5,pady=20)

         #Export csv button
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        export_btn.grid(row=0,column=1,padx=5,pady=20)

         #Update button
        update_btn=Button(btn_frame,text="Update",width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        update_btn.grid(row=0,column=2,padx=5,pady=20)

         #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",16,"bold"),bg="white",fg="black")
        reset_btn.grid(row=0,column=3,padx=5,pady=20)


        #right frame
        right_frame = LabelFrame(main_frame, bd=2, width=70,relief=RIDGE, text="Attendance Details", font=("times new roman", 20, "bold"), bg="lightgray",fg="blue")
        right_frame.place(x=740, y=100, width=650, height=750)

        table_frame=LabelFrame(right_frame,bd=2,bg="white",fg="black",relief=RIDGE)
        table_frame.place(x=15,y=5,width=620,height=690)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_report_table=ttk.Treeview(table_frame,column=("sid","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendance_report_table.xview)
        scroll_y.config(command=self.attendance_report_table.yview)

        self.attendance_report_table.column("#0", width=0, stretch=NO)

        self.attendance_report_table.heading("sid", text="Attendance Id")
        self.attendance_report_table.heading("roll", text="Roll")
        self.attendance_report_table.heading("name", text="Name")
        self.attendance_report_table.heading("dep", text="Department")
        self.attendance_report_table.heading("time", text="Time")  
        self.attendance_report_table.heading("date", text="Date")  
        self.attendance_report_table.heading("attendance", text="Attendance")
        self.attendance_report_table["show"]="headings"

        self.attendance_report_table.pack(fill=BOTH,expand=1)
        self.attendance_report_table.bind("<ButtonRelease>",self.get_cursor)

    #------fetch data-------
    def fetch_data(self,rows):
        self.attendance_report_table.delete(*self.attendance_report_table.get_children())
        for i in rows:
            self.attendance_report_table.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open (fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as e:
            messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)

    #-----get_cursor function-----
    def get_cursor(self,event=""):
        cursor_row=self.attendance_report_table.focus()
        content=self.attendance_report_table.item(cursor_row)
        rows=content['values']
        self.var_attId.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_attId.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")


        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
