from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("530x790+0+0") #0 denote x, y axis
        self.root.title("I-BioFin")

        #self.root.configure(background='beige')
        root.resizable(False, False)
         

        # self.bg=ImageTk.PhotoImage(file=r"./Images/background.jpg")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)



        frame=Frame(self.root,bg="alice blue")
        frame.place(x=0,y=0,width=530,height=790)

        img1=Image.open(r"C:\Users\rakib\OneDrive\Documents\GitHub\python-desktop-app_projects\Images\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=0,y=0,width=340,height=450)




if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

        