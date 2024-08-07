from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System, speak_va
from time import strftime

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        #first
        img=Image.open(r"college_images\u.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second
        img1=Image.open(r"college_images\college.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third
        img2=Image.open(r"college_images\u.jpg")
        img2=img2.resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

        #bg image
        img3=Image.open(r"college_images\hackers2.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="teal",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #time
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl= Label(title_lbl,font=("times new roman",10,"bold"),bg='teal',fg='black')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #frame
        frame = Frame(self.root, bg="black",relief="ridge",highlightthickness=3,highlightbackground='lightskyblue')
        frame.place(x=610, y=220, width=340, height=450)

        img1 = Image.open(r"college_images\dev.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=225, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg="black", fg="white")
        get_str.place(x=100, y=100)

        # labels
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="black", fg="white")
        username_lbl.place(x=65, y=152)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password_lbl.place(x=65, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        #icon images
        img2 = Image.open(r"college_images\dev.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=373, width=25, height=25)

        img3 = Image.open(r"college_images\lock-512.png")
        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=447, width=25, height=25)

        # loginBuutton
        img4=Image.open(r"college_images\8.jpg")
        img4=img4.resize((120,35),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        loginbtn = Button(frame,image=self.photoimg4, command=self.login,bg="black")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # registrationButton
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, bg="black", fg="white", activebackground="black")
        registerbtn.place(x=20, y=350, width=160)

        # forgetpasswordButton
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, bg="black", fg="white", activebackground="black")
        forgetbtn.place(x=20, y=380, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "afrin" or "afrin" and self.txtpass.get() == "afrin@123":
            speak_va("Welcome to Face Recognition World")
            messagebox.showinfo("success", "welcome to Face Recognition World")
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_System(self.new_window)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Afrin@123", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()

                     ))
            row=my_cursor.fetchone()
            if row==None:
                speak_va("Invalid username and password!")
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
 
    #============================================reset password============================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
                messagebox.showerror("Error","select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
                messagebox.showerror("Error","select your answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
                messagebox.showerror("Error","please enter your new password",parent=self.root2) 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Afrin@123", database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s ")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
      
            row=my_cursor.fetchone()
            if row==None:
                speak_va("Wrong Security Answer")
                messagebox.showerror("Error","Invalid security answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                speak_va("Your password has been reset successfully.")
                messagebox.showinfo("Info","your password has been reset , please login new password",parent=self.root2)
            conn.commit()
            conn.close()
            self.root2.destroy()
               
#============================================forget password============================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Afrin@123", database="face_recognizer")
            
            my_cursor = conn.cursor()
            query=("select *from register where email=%s")  
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"),bg="white", fg="red")
                l.place(x=0,y=0,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "your dad name", "your mother name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="orange",fg="green")
                btn.place(x=100,y=300)

#============================================Register============================================ 
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1530x790+0+0")

        #variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        bg=Image.open(r"college_images\hackers2.jpg")
        bg=bg.resize((1530,790),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)

        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0,relwidth=1, relheight=1)
        
        # #left image
        self.bg1 = ImageTk.PhotoImage(file=r"college_images\6.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=100, y=100, width=400, height=500)

        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=700, height=500)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="teal", bg="white")
        register_lbl.place(x=50, y=30)

        # lebel and entry
        Register_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="REGISTER HERE",font=("times new roman",20,"bold"), fg="dark blue")
        Register_frame.place(x=5,y=5,width=670,height=400)
        
        fname=Label(Register_frame,text="First and Middle Name",font=("times new roman",15,"bold"),bg="white")
        fname.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        fname_entry=ttk.Entry(Register_frame,textvariable=self.var_fname,width=25,font=("times new roman",13,"bold"))
        fname_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        validate_fname=self.root.register(self.checkname)
        fname_entry.config(validate='key',validatecommand=(validate_fname,'%P'))

    
        lname=Label(Register_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        lname_entry=ttk.Entry(Register_frame,textvariable=self.var_lname,width=25,font=("times new roman",13,"bold"))
        lname_entry.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        validate_lname=self.root.register(self.checklname)
        fname_entry.config(validate='key',validatecommand=(validate_lname,'%P'))


        contact=Label(Register_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        contact_entry=ttk.Entry(Register_frame,textvariable=self.var_contact,width=25,font=("times new roman",13,"bold"))
        contact_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        validate_phone=self.root.register(self.checkphone)
        contact_entry.config(validate='key',validatecommand=(validate_phone,'%P'))

        email=Label(Register_frame,text="Email or Username",font=("times new roman",15,"bold"),bg="white")
        email.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Register_frame,textvariable=self.var_email,width=25,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        email=Label(Register_frame,text="*Please enter valid email: ex123@gmail.com",font=("times new roman",8,"bold"),fg="red",bg="white")

        email.place(x=250, y=139)

        security_Q=Label(Register_frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        Security_combo=ttk.Combobox(Register_frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly",width=23)
        Security_combo["values"]=("Select Security Question","Your birth place","Your Dad's Name","Your Mom's name")
        Security_combo.current(0)
        Security_combo.grid(row=7,column=1,padx=5,pady=10,sticky=W)

        security_A=Label(Register_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.grid(row=6,column=2,padx=10,pady=5,sticky=W)

        security_entry=ttk.Entry(Register_frame,textvariable=self.var_securityA,width=25,font=("times new roman",13,"bold"))
        security_entry.grid(row=7,column=2,padx=10,pady=5,sticky=W)

        pswd=Label(Register_frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.grid(row=8,column=1,padx=10,pady=5,sticky=W)

        pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_pass,width=25,font=("times new roman",13,"bold"))
        pswd_entry.grid(row=9,column=1,padx=10,pady=5,sticky=W)


        pswd=Label(Register_frame,text="*Please enter strong password",font=("times new roman",10,"bold"),fg="red",bg="white")
     
        pswd.place(x=35, y=305)

        confirm_pswd=Label(Register_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.grid(row=8,column=2,padx=10,pady=5,sticky=W)

        confirm_pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_confpass,width=25,font=("times new roman",13,"bold"))
        confirm_pswd_entry.grid(row=9,column=2,padx=10,pady=5,sticky=W)

        #============================================check button============================================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I am Agree with terms and conditions", font=(
            "times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=370)

        #button
        img = Image.open(r"college_images\7.jpg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=50, y=420, width=200)

        img1 = Image.open(r"college_images\8.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login,borderwidth=0, cursor="hand2")
        b1.place(x=350, y=420, width=200)


    def checkname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checklname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checkphone(self,phone):
        if len(phone) <=10:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
            messagebox.showerror('Invalid','Invalid entry. Please enter phone (example:9846200045)', parent=self.root)
            return False
            
        else:
            messagebox.showwarning('Alert','invalid phone. Please enter phone (example:9846200045)',parent=self.root)
            return False


     #============================================fuction declarations============================================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            speak_va("All fields are required")
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password and confirm password must be same",parent=self.root)
        
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions",parent=self.root)
        
        elif not ("@" or ".com") in self.var_email.get():
            messagebox.showerror("Error",'Invalid email Enter valid email.',parent=self.root)

        
        elif not ("@" or "!" or "$" or "-" or "." or "#" ) in self.var_pass.get():
            messagebox.showerror("Error",'Invalid password Please Enter Strong password',parent=self.root)


        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
      
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s") 
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                speak_va("user already exist")
                messagebox.showerror("Error", "user already exists ,try another email", parent=self.root )
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
               
            conn.commit()
            conn.close()
            speak_va("Registered Successfully!!")
            messagebox.showinfo("Success", "Register Successfully", parent=self.root )
    def return_login(self):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()        

