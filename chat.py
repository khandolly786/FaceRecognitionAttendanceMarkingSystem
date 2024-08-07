from tkinter import*
from tkinter import ttk
from webbrowser import get
from PIL import Image, ImageTk

class chatbot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("730x620+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()

        img= Image.open("college_images\chat.jpg")
        img = img.resize((200,70),Image.ANTIALIAS)  
        self.photoimg=ImageTk.PhotoImage(img)

        title_lbl=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=("Algerian",30,"bold"),fg='black',bg='teal')
        title_lbl.pack(side="top")

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('sans',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        label=Label(btn_frame,text="Type Something",font=("times new roman",14,"bold"),fg="steel blue",bg="white")
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=37,font=("times new roman",16,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.Send,width=8,font=("times new roman",15,"bold"),bg="teal")
        self.send.grid(row=0,column=3,padx=5)

        self.clear=Button(btn_frame,text="clear Data",command=self.clear,width=8,font=("times new roman",15,"bold"),bg="teal")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label1=Label(btn_frame,text=self.msg,font=("times new roman",14,"bold"),fg="steel blue",bg="white")
        self.label1.grid(row=1,column=1,padx=5,sticky=W)

    
#=======================================function declaration=============================================================

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def Send(self):
        send='\t\t\t'+'you: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry,get()==''):
            self.msg='Please enter some input'
            self.label1.config(text=self.msg,fg='red')
        
        else:
            self.msg=''
            self.label1.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot:Hello')

        elif(self.entry.get()=='how are you?'):
            self.text.insert(END,'\n\n'+'Bot:fine and you')

        elif(self.entry.get()=='fantastic'):
            self.text.insert(END,'\n\n'+'Bot:Nice to hear ')

        elif(self.entry.get()=="what is your name?"):
            self.text.insert(END,'\n\n'+"Bot:my name is IEM,Bot")

        elif(self.entry.get()=="Bye"):
            self.text.insert(END,'\n\n'+"Bot:Thank You for chatting")

        elif(self.entry.get()=="bye"):
            self.text.insert(END,'\n\n'+"Bot:Thank You for chatting")

        elif(self.entry.get()=="Can you speak hindi?"):
            self.text.insert(END,'\n\n'+"Bot:I am still learning.")

        elif(self.entry.get()=="what is this project about?"):
            self.text.insert(END,'\n\n'+"Bot:This is a student management \nsystem which can be used by \ncollegees or schools to track \nthe attendance of students using \nfacial recognition.")

        elif(self.entry.get()=='how can we make attendance in this?'):
            self.text.insert(END,'\n\n'+"Bot:you can make attendance \nby going to face recognition page.")

        elif(self.entry.get()=="Who created this project?"):
            self.text.insert(END,'\n\n'+"Bot:Shahin ceated this project\nfor submisssion in microsoft\n engage'2022")    

        else:
            self.text.insert(END,'\n\n'+"Bot:sorry i didn't get it")


if __name__=="__main__":
    root=Tk()
    obj=chatbot(root)
    root.mainloop()