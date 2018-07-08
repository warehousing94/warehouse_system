# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 13:12:58 2018

@author: Fatemeh
"""
import sys
sys.path.append(r"C:\Users\asus\Desktop\warehouseSystem\Model")
from pyodbc import *
import pandas as pd
from Manager import Manager
from Warehouse import Warehouse
from Company import Company
from Settings import Setting
sting = Setting()


class ManagerAction(object):
    
    
    def signUp(self, Manager):
         SQLCommand = ("INSERT INTO Manager"
                      "(username, password, email)"
                      " VALUES ('%s','%s','%s')"
                      %(Manager.username,Manager.password , Manager.email))    
         sting.cursor.execute(SQLCommand)
         sting.connection.commit()
    
    def addWarehouse(self,Manager , Warehouse,Company):
        SQLCommand = ("INSERT INTO Warehouse "
                 "(WarehouseName, Capacity, Username, Password, Email, CompanyName)"
                 "VALUES ('%s','%s','%s','%s','%s','%s')"%
                         (Warehouse.name,Warehouse.capacity,Manager.username,
                          Manager.password, Manager.email, Company.name))
        
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
    
        
    def delWarehouse(self, Warehouse, Company):
        SQLCommand = ("DELETE FROM Warehouse WHERE WarehouseName='%s' and Capacity='%s'"%(Warehouse.name,Warehouse.capacity))
        
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
      
    
    def editWarehouse(self, Warehouse,newName,newCapacity):
        SQLCommand = ("UPDATE Warehouse SET WarehouseName='%s',Capacity='%s' WHERE WarehouseName='%s' and Capacity='%s'"%(newName,newCapacity,Warehouse.name,Warehouse.capacity))
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()             
                      
    
    def showWarehouse(self,Manager):
        query=("SELECT * FROM Warehouse WHERE Username='%s' and Password='%s' and Email='%s'"%
                     (self.getUsername(Manager),self.getPassword(Manager),
                      self.getEmail(Manager)))
        sting.cursor.execute(query)
        results = sting.cursor.fetchall()
        for row in results:
            r=str(row)
            removed = r.replace("u'", "")
            removed2 = removed.replace("'", "")
            print str(removed2)
        
    def showAllCompanies(self):
       query=("SELECT CompanyName FROM Company")
       sting.cursor.execute(query)
       results = sting.cursor.fetchall()
       for row in results:
            r=str(row)
            removed = r.replace("u'", "")
            removed2 = removed.replace("'", "")
            print str(removed2)
  
    def getUsername(self,Manager):
        return Manager.username
        
    def getPassword(self,Manager):
        return Manager.password
        
    def getEmail(self,Manager):
        return Manager.email
    
       
    
    
