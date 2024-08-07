from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
import cv2
from datetime import datetime
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Algerian",20,"bold"),bg="lightblue",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=55)

       #first image
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
        # second image
        img_bottom=Image.open(r"college_images\face_detector2.jpg")
        img_bottom = img_bottom.resize((950, 700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        # Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Algerian",15,"bold"),bg="teal",fg="black")
        b1_1.place(x=365,y=620,width=220,height=40)


        # ==========================================Attendance===============================================
    def mark_attendance(self,i,r,n,d):
        with open("data.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split(" ")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString}, {d1},Present{i}")
            

    #===============================================face recognition======================================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)   

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
            
                conn=mysql.connector.connect(host="localhost",username="root",password="Afrin@123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where id="+str(id))
                n= my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where id="+str(id))
                r=my_cursor.fetchone()
                r= "+".join(r)
                
                my_cursor.execute("select Dep from student where id="+str(id))
                d=my_cursor.fetchone()
                d= "+".join(d)

                my_cursor.execute("select id from student where id="+str(id))
                i=my_cursor.fetchone()
                i = "+".join(i)
                
                if predict < 500:
                    confidence=int((100*(1-predict/300)))
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)

                if confidence>77:
                    cv2.putText(img,f"id: {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,0,255),3)
                    speak_va("Warning!!! Unknown Face")
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord 
            
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)   
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)


            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

      
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()