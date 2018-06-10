import Tkinter as Tk
 

class MyApp(object): 
    
    def __init__(self, parent):
        self.root = parent
        self.root.geometry("800x500")
        self.root.title('warehouse System')
        self.root.configure(background="white")
        
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        
        w = Tk.Label(self.frame, text="Warehouse System",bg="white", font = "bnazanin 20 bold ")
        w.place(relwidth = 0.5, relheight = 0.2, relx = 0.25, rely = 0.15)
        w.pack()
        
        w2 = Tk.Label(self.frame, text="Choose one of the below item to continue",bg="white", font = "bnazanin 15 bold ")
        w2.place(relwidth = 0.5, relheight = 0.05, relx = 0.25, rely = 0.35)
        w2.pack()
        
        v=Tk.IntVar() 
        r1 = Tk.Radiobutton(self.frame,text="Company",padx=20,variable=v,value=1,bg="white",font = "bnazanin 11 bold ",command=lambda:self.admin_login())
        r1.place(relwidth = 0.5, relheight = 0.1, relx = 0.25, rely = 0.42)
        r1.pack()
        #btn1=Tk.Button(self.frame, text="company", command=handler)
        r2 = Tk.Radiobutton(self.frame,text="Client",padx=20,variable=v,value=2,bg="white",font = "bnazanin 11 bold ",command=lambda:self.client_login())
        r2.place(relwidth = 0.5, relheight = 0.1, relx = 0.25, rely = 0.5)
        r2.pack()
        x = v.get()
        
    def openFrame(self,barname):
        
        otherFrame = Tk.Toplevel()
        otherFrame.geometry("800x500")
        otherFrame.title("otherFrame")
        
        background_image = Tk.PhotoImage(file="4.gif")
        background_label =Tk.Label(otherFrame, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        handler = lambda:self.onCloseOtherFrame(otherFrame, barname)
        
        btn = Tk.Button(otherFrame, text="Close", command=handler)
        btn.place(relwidth = 0.2, relheight = 0.07, relx = 0.4, rely = 0.85)
        
        barname.destroy()
        
    def onCloseOtherFrame(self,otherFrame,barname):
        otherFrame.destroy()
        self.show(barname)
    
    def show(self,root):
        root.update()
        root.deiconify()
        
    def checkradio(self,x):
        #x = v.get()
        print(x)
        if(x == 2):
            print("2")
            self.client_login()
        if(x == 1):
            print("1")
            self.admin_login()
    def hide(self):
        """"""
        self.root.withdraw()
    def client_login(self):
        #self.root.destroy()
        self.hide()
        clientlogin = Tk.Toplevel()
        clientlogin.geometry("800x500")
        clientlogin.title('warehouse System')
        background_image=Tk.PhotoImage(file="4.gif")
        background_label = Tk.Label(clientlogin, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        w = Tk.Label(clientlogin, text = "Warehouse System Login for client",bg = "white", font = "bnazanin 24 bold ")
        w.place(relwidth = 0.9, relheight = 0.1, relx = 0.05, rely = 0.3)
        Tk.Label(clientlogin,text="Username").place(relwidth = 0.07, relheight = 0.05, relx = 0.53, rely = 0.5)
        e = Tk.Entry(clientlogin)
        e.place(relwidth = 0.16, relheight = 0.05, relx = 0.35, rely = 0.5)
        Tk.Label(clientlogin,text="Password").place(relwidth = 0.07, relheight = 0.05, relx = 0.53, rely = 0.59)
        e2 = Tk.Entry(clientlogin)  
        e2.place(relwidth = 0.16, relheight = 0.05, relx = 0.35, rely = 0.59)
        button=Tk.Button(clientlogin,text='login',width=25,command = lambda:self.on_button(e,e2,"client","client",clientlogin))
        button.place(relwidth = 0.16, relheight = 0.05, relx = 0.35, rely = 0.7)
        self.root.grab_set()
    def admin_login(self):
        #self.root.destroy()
        self.hide()
        barname = Tk.Tk()
        barname.geometry("800x500")
        barname.title('warehouse System')
        barname.configure(background="white")
    
        w = Tk.Label(barname, text="Warehouse System Login for Company",bg="white", font = "bnazanin 24 bold ")
        w.place(relwidth = 0.9, relheight = 0.1, relx = 0.05, rely = 0.3)
        Tk.Label(barname,text="Username").place(relwidth = 0.07, relheight = 0.05, relx = 0.53, rely = 0.5)
        
        e = Tk.Entry(barname)
        e.place(relwidth = 0.16, relheight = 0.05, relx = 0.35, rely = 0.5)
        Tk.Label(barname,text="Password").place(relwidth = 0.07, relheight = 0.05, relx = 0.53, rely = 0.59)
        
        e2 = Tk.Entry(barname)  
        e2.place(relwidth = 0.16, relheight = 0.05, relx = 0.35, rely = 0.59)
        button = Tk.Button(barname,text='login',width=25,command = lambda:self.on_button(e,e2,"admin","admin",barname))
        button.place(relwidth = 0.16, relheight = 0.05, relx = 0.35, rely = 0.7)
        self.root.grab_set()
    
    
    def on_button(self,e,e2,s1,s2,barname):
        if (e.get().strip().lower()==s1):
            if(e2.get().strip().lower()==s2):
                if(s1=="admin"):
                    self.openFrame(barname)
                else:
                    self.openclientFrame(barname)
            print("enter password!!")
    
    
    def openclientFrame(self,barname):
        clientFrame = Tk.Toplevel()
        clientFrame.geometry("800x500")
        clientFrame.title("otherFrame")
        clientFrame.configure(background = "white")
        btn = Tk.Button(clientFrame, text = "Close", command = clientFrame.destroy)
        btn.place(relwidth = 0.2, relheight = 0.07, relx = 0.4, rely = 0.85)
        barname.destroy()       


if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()















