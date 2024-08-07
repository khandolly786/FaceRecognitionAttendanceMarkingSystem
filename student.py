from tkinter import*
from tkinter import ttk
import cv2
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #variable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()
        self.var_teacher=StringVar()


        #first
        img=Image.open(r"college_images\student1.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second
        img1=Image.open(r"college_images\student2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third
        img2=Image.open(r"college_images\student3.jpg")
        img2=img2.resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)
 
        #bg image
        img3=Image.open(r"college_images\clock.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="teal",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)

        img_left=Image.open(r"college_images\student4.jpg")
        img_left=img_left.resize((710,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=710,height=130)
 
        #CURRENT COURSE
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=710,height=115)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","B.tech","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=710,height=300)

        #student id
        student_Id_label=Label(Class_Student_frame,text="Student ID",font=("times new roman",13,"bold"),bg="white")
        student_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentname_label=Label(Class_Student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        validate_name=self.root.register(self.checkname)
        studentname_entry.config(validate='key',validatecommand=(validate_name,'%P'))

        #class division
        clas_div_label=Label(Class_Student_frame,text="Class Divisions",font=("times new roman",13,"bold"),bg="white")
        clas_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="read only",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        Roll_no_label=Label(Class_Student_frame,text="Roll No",font=("times new roman",13,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        validate_roll=self.root.register(self.checkroll)
        Roll_no_entry.config(validate='key',validatecommand=(validate_roll,'%P'))


        #Gender
        Gender_label=Label(Class_Student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        DOB_label=Label(Class_Student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        cal = DateEntry(Class_Student_frame,textvariable=self.var_DOB, width=23, year=2003, month=7, day=22, 
         background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=2,column=3,padx=10, pady=10)

        #Email
        Email_label=Label(Class_Student_frame,text="Email ID",font=("times new roman",13,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        email=Label(Class_Student_frame,text="*ex123@gmail.com",font=("times new roman",6,"bold"),fg="red",bg="white")
        email.place(x=150, y=149)

        #Phone no
        Phone_no_label=Label(Class_Student_frame,text="Phone NO",font=("times new roman",13,"bold"),bg="white")
        Phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        Phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        validate_phone=self.root.register(self.checkphone)
        Phone_no_entry.config(validate='key',validatecommand=(validate_phone,'%P'))

        #Address
        Address_label=Label(Class_Student_frame,text="Address",font=("times new roman",13,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        validate_address=self.root.register(self.checkaddress)
        Address_entry.config(validate='key',validatecommand=(validate_address,'%P'))

        #Teacher Name
        teacher_name_label=Label(Class_Student_frame,text="Teacher Name",font=("times new roman",13,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        validate_Teacher=self.root.register(self.checkTeachername)
        teacher_name_entry.config(validate='key',validatecommand=(validate_Teacher,'%P'))

        #radio buttons 
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=700,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new romn",13,"bold"),bg="teal",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new romn",13,"bold"),bg="teal",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new romn",13,"bold"),bg="teal",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new romn",13,"bold"),bg="teal",fg="black")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=700,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=34,font=("times new romn",13,"bold"),bg="teal",fg="black")
        take_photo_btn.grid(row=0,column=0)

        Update_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Update Photo",width=34,font=("times new romn",13,"bold"),bg="teal",fg="black")
        Update_photo_btn.grid(row=0,column=1)

       #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=740,y=10,width=720,height=580)

        img_right=Image.open(r"college_images\student4.jpg")
        img_right=img_right.resize((710,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=710,height=130)

        #search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search student information",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",13,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","roll","phone","id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn=Button(search_frame,command=self.search_data,text="Search",width=12,font=("times new romn",12,"bold"),bg="teal",fg="black")
        Search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=12,font=("times new romn",12,"bold"),bg="teal",fg="black")
        showall_btn.grid(row=0,column=4,padx=4)
 
        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","DOB","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")       
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

     #===================================================function declaration===================================
    def add_data(self):
        if (self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()==""):
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #====================================================fetch data==================================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

    #====================================================GET CURSOR====================================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #====================================================update function====================================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            speak_va('Alert!!! All fields are required.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        else:
            try:
                speak_va("Do you want to Update this Student's Details?")
                Upadate = messagebox.askyesno("Upadate","Do You Want To Update This Student Details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set dep=%s,course=%s,Year=%s,Sem=%s,name=%s,roll=%s,gender=%s,DOB=%s,email=%s,phone=%s,address=%s,teacher=%s,Photo=%s where id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()  ,
                                                                                                                self.va_std_id.get() 
                                                                                                            ))   
                
                else:
                    if not Upadate:
                        return
                speak_va('Student Details updated successfully.')
                messagebox.showinfo("Success","Student Details updated Successfully.",parent=self.root)                                                                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #====================================================delete function====================================================
    def delete_data(self):    
        if self.va_std_id.get()=="" :
            speak_va('student id required!')
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                speak_va('do you want to delete this page?')
                delete=messagebox.askyesno("delete","do you want to delete this student page",parent=self.root)
                if delete>0:   
                    conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close() 
                speak_va("Deleted successfully!!!") 
                messagebox.showinfo("delete","successfully deleted student details",parent=self.root)      
            except Exception as es:
                speak_va("An Exception Occurred!")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    #====================================================reset====================================================
    def reset_data(self):
        self.var_dep.set("select department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_sem.set("select semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select division")
        self.var_roll.set("")
        self.var_gender.set("select gender")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
       
     #====================================================search data====================================================   
    def search_data(self):
        if self.var_search.get()=="" or self.var_com_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        speak_va("Data Not Found")
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                speak_va("An Exception Occurred!")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #====================================================take photo====================================================
    def generate_dataset(self):
        if (self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()==""):
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s ,course=%s ,year=%s ,sem=%s ,name=%s,roll=%s ,gender=%s ,DOB=%s ,email=%s ,phone=%s ,address=%s ,teacher=%s ,photo=%s  where id=%s ",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.va_std_id.get()==id+1
                                                                                                            ))    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
                #=============================load predefined data on face frontals from opencv=======================
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()   
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                       
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255,0),2)
                        cv2.imshow("cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                speak_va('Generating data sets completed!!')
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                speak_va("An Exception Occurred!")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #====================================================call back sytem====================================================
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            speak_va('Invalid! Name Not allowed.')
            messagebox.showerror('Invalid','Not allowed' +name[-1])
    def checkname(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True
    
    def checkaddress(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True

    def checkTeachername(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
               return False
              
       return True
       

    #============================================checkphone number======================================
    def checkphone(self,phone):
        if len(phone) <=10:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
              speak_va('Invalid phone number Format')
              messagebox.showerror('Invalid','Invalid entry. Please enter phone (example:9846200045)')
              return False
            
        else:
            speak_va('Alert!!! Invalid Phone Number')
            messagebox.showwarning('Alert','invalid phone. Please enter phone (example:9846200045)')
            return False

    #====================================================Id_no validation==================================================== 
    def checkid(self,id):
        if len(id) <=5:
          if id.isdigit():
            return True
          if len(str(id))==0:
            return True
          else:
              speak_va('Invalid ID. Please enter ID as integer value')
              messagebox.showerror('Invalid','Invalid entry ID. Please enter ID as integer value (example: ID :- 1 2 3 4 5 6 7...like this)')
              return False
        else:
            speak_va('Invalid ID.')
            messagebox.showwarning('Alert','invalid ID. Please Enter valid ID.')
            return False

    #============================================Roll_no validation===================================
    def checkroll(self,roll):
        if len(roll) <=6:
          if roll.isdigit():
            return True
          if len(str(roll))==0:
            return True
          else:
              speak_va('Invalid Roll number. Please Enter your valid roll number.')
              messagebox.showerror('Invalid','Invalid entry enter Roll No (example: Roll No: 171346)')
              return False
        else:
            speak_va('Invalid Roll number.')
            messagebox.showwarning('Alert','invalid phone enter Roll No (example: Roll No: 171346)')
            return False
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()