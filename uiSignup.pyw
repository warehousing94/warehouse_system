from pyodbc import *
from Tkinter import*
import pandas as pd


class Setting():
    def __init__(self):
            self.connection = connect(r'Driver={SQL Server};Server=DESKTOP-T60JE22\MYSQLSERVER;Database=WarehouseSystem;Trusted_Connection=yes;')
            self.cursor = self.connection.cursor()
        #sting=Setting()barname=Tk()
            window = Tk()
            window.geometry("800x500")
            window.title('warehouse System')
            window.configure(background="white")
            frame = Frame(window)
            frame.pack()
            
            self.fields = {}
            
            l = Label(frame, text="Name:")
            l.grid(row=0, column=0)
            self.fields['name'] = Entry(frame)
            self.fields['name'].grid(row=0, column=1)           
            l = Label(frame, text="Email:")
            l.grid(row=2, column=0)
            self.fields['phone'] = Entry(frame)
            self.fields['phone'].grid(row=2, column=1)  
            l = Label(frame, text="Address:")
            l.grid(row=4, column=0)
            self.fields['address'] = Entry(frame)
            self.fields['address'].grid(row=4, column=1)      
            submitbtn = Button(frame, text="Insert", command=self.do_insert)
            submitbtn.grid(row=11, column=0)           
            clearbtn = Button(frame, text="Clear", command=self.do_clear)
            clearbtn.grid(row=11, column=1)
            window.mainloop()
    def do_clear(self):
        self.fields['name'].delete(0,END)
        self.fields['phone'].delete(0,END)
        self.fields['address'].delete(0,END)
    def do_insert(self):
        #sql = "insert into Users set UserName='%s', UserPhone='%s', UserAddress='%s'"%(self.fields['name'].get(),self.fields['phone'].get(),self.fields['address'].get())
        sql = ("INSERT INTO Users"
                      "(User_Name, User_Phone, User_Address)"
                      " VALUES ('%s','%s','%s')"%(self.fields['name'].get(),self.fields['phone'].get(),self.fields['address'].get()))
        print sql
        self.cursor.execute(sql)
        self.connection.commit()
if __name__=="__main__":
    Setting()
    
    
    
    
    
    
    
    
    
    
    
