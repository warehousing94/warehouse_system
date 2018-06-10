# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:07:50 2018

@author: asus
"""

from pyodbc import *
from Tkinter import*
import pandas as pd


class Setting():
    def __init__(self):
            self.connection = connect(r'Driver={SQL Server};Server=DESKTOP-T60JE22\MYSQLSERVER;Database=WarehouseSystem;Trusted_Connection=yes;')
            self.cursor = self.connection.cursor()

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
            l = Label(frame, text="pass:")
            l.grid(row=2, column=0)
            self.fields['pass'] = Entry(frame, show="*")
            self.fields['pass'].grid(row=2, column=1)  
    
            submitbtn = Button(frame, text="Insert", command=self.do_insert)
            submitbtn.grid(row=11, column=0)           
            clearbtn = Button(frame, text="Clear", command=self.do_clear)
            clearbtn.grid(row=11, column=1)

            window.mainloop()
    def do_clear(self):
        self.fields['name'].delete(0,END)
        self.fields['pass'].delete(0,END)

    def do_insert(self):
        sql=("SELECT User_Name FROM Users WHERE User_Name = '%s'"%(self.fields['name'].get()))
        print sql
        self.cursor.execute(sql)

        row1=self.cursor.fetchone()
        r=str(row1)
 
        removed = r.replace("(u'", "")
        removed2 = removed.replace("', )", "")
        #-----------------------------------------------------------------------
        sql2=("SELECT User_Phone FROM Users WHERE User_Phone = '%s'"%(self.fields['pass'].get()))

        self.cursor.execute(sql2)

        row2=self.cursor.fetchone()
        r2=str(row2)

        removedp = r2.replace("(u'", "")
        removed2p = removedp.replace("', )", "")
        if(removed2p==self.fields['pass'].get()):
            if(removed2==self.fields['name'].get()):
                 print "success !"
        else:
            print "fail !"
        self.connection.commit()
if __name__=="__main__":
    Setting()
    
    
    
    
    
    
    
    
    
    
    
