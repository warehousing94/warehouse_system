# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 13:12:58 2018

@author: Fatemeh
"""
import sys
sys.path.append(r"C:\Users\Fatemeh\Desktop\warehouseSystem\Model")
from pyodbc import *
import pandas as pd
from Manager import Manager
from Warehouse import Warehouse
from Company import Company


class ManagerAction(object):
    
    
    def signUp(self, Manager):
         SQLCommand = ("INSERT INTO Manager"
                      "(username, password, email)"
                      " VALUES ('%s','%d','%s')"
                      %(Manager.username,Manager.password , Manager.email))    
         
    
    def addWarehouse(self,Manager , Warehouse,Company):
        SQLCommand = ("INSERT INTO Warehouse "
                 "(WarehouseName, Capacity, Username, Password, Email, ComapanyName)"
                 "VALUES ('%s','%f','%s','%d','%s','%s')"%
                         (Warehouse.name,Warehouse.capacity,self.getUsername(Manager),
                          self.getPassword(Manager), self.getEmail(Manager), Company.name))
       
    
        
    def delWarehouse(self, Warehouse, Company):
        SQLCommand = ("DELETE FROM Warehouse WHERE "
                      "(WarehouseName, Capacity)"
                      "VALUES ('%s','%f')"%
                       (Warehouse.name,Warehouse.capacity))
        
      
    
    def editWarehouse(self, Warehouse,newName,newCapacity):
        SQLCommand = ("UPDATE Warehouse SET WarehouseName=%s,Capacity=%f WHERE WarehouseName=%s, Capacity=%f"
                     %(newName,newCapacity,Warehouse.name,Warehouse.capacity))
                     
                      
    
    def showWarehouse(self,Manager):
        warehouseData = pd.read_sql("SELECT * FROM Warehouse WHERE"
                     "(Username, Password, Email)"
                     "VALUES ('%s','%d','%s')"%
                     (self.getUsername(Manager),self.getPassword(Manager),
                      self.getEmail(Manager)))
        return warehouseData
        
    def showAllCompanies(self):
       ListOfCompanies = pd.read_sql("SELECT CompanyName FROM Company")
       return ListOfCompanies
        
    def connectDB(self):
        self.connection = connect(r'Driver={SQL Server};Server=DESKTOP-6QFOIGQ\FATEMEH;Database=WarehouseSystem;Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()
        
    def getUsername(self,Manager):
        return Manager.username
        
    def getPassword(self,Manager):
        return Manager.password
        
    def getEmail(self,Manager):
        return Manager.email
    
        
    
    