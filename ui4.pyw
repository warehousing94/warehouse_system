from pyodbc import *
from Tkinter import*
import pandas as pd
barname=Tk()
barname.geometry("800x500")
barname.title('warehouse System')
barname.configure(background="white")
listbox=Listbox(barname)
listbox.place(relwidth = 0.8, relheight = 0.5, relx = 0.1, rely = 0.3)
i=0
class Setting():
    def __init__(self):
        self.connection = connect(r'Driver={SQL Server};Server=DESKTOP-T60JE22\MYSQLSERVER;Database=WarehouseSystem;Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()
    #sting=Setting()
        SQLCommand2="SELECT * FROM Warehouse"
        self.cursor.execute(SQLCommand2)
        w = Label(barname, text="Warehouse System",bg="white", font = "bnazanin 24 bold ")
        w.place(relwidth = 0.9, relheight = 0.1, relx = 0.05, rely = 0.1)
        for row in self.cursor:
                print(row[0],row[1],row[2],row[3],row[4])
                w=str(row[0])+"                    "+str(row[1])+"                         "+str(row[2])+"                         "+str(row[3])+"             "+str(row[4])
                listbox.insert(END,w)
                
        self.connection.commit()
       # for item in ["text1","text2","text3"]:
        mainloop()
