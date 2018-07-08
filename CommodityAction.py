# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 16:14:08 2018

@author: Fatemeh
"""
import sys
sys.path.append(r"C:\Users\asus\Desktop\warehouseSystem\Model")
from pyodbc import *
from Warehouse import Warehouse
from Commodity import Commodity
import pandas as pd
from Settings import Setting
sting = Setting()
num=0
class CommodityAction(object):
    def addCommodity(self,Commodity, Warehouse):
        SQLCommand =  ("INSERT INTO Commodity"
                      "(CommodityName ,Type ,number ,price , WarehouseName)"
                      " VALUES ('%s','%s','%d','%s','%s')"%(Commodity.name ,Commodity.Type ,Commodity.number ,Commodity.price,Warehouse.name))
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
        
        
    def reduceCommodity(self,Commodity,numOfLost,Warehouse):
        number = self.getNumber(Commodity) - numOfLost
        SQLCommand = ("UPDATE Commodity SET number=%d WHERE CommodityName='%s' and Type='%s' and number=%d and price='%s' and WarehouseName='%s'" 
                      %(number,self.getName(Commodity) ,self.getType(Commodity),self.getNumber(Commodity) ,self.getPrice(Commodity) ,Warehouse.name))
        
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
        
    def delCommodity(self,Commodity, Warehouse):
        SQLCommand = ("DELETE FROM Commodity WHERE CommodityName='%s' and Type='%s' and number=%d and price='%s' and  WarehouseName='%s' "%(Commodity.name ,Commodity.Type ,Commodity.number ,Commodity.price,Warehouse.name))
        
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
        
    def editCommodity(self, Commodity, newName, newType, newNumber, newPrice, Warehouse):
         SQLCommand = ("UPDATE Commodity SET CommodityName='%s' , Type='%s' , number=%d , price='%s' WHERE CommodityName='%s' and Type='%s' and number=%d and price='%s' and WarehouseName='%s'"
                       %(newName, newType, newNumber, newPrice,self.getName(Commodity) ,self.getType(Commodity),self.getNumber(Commodity) ,self.getPrice(Commodity) ,Warehouse.name))
                      
         sting.cursor.execute(SQLCommand)
         sting.connection.commit()
             
    def getTotalNumOfCommodity(self,Warehouse):
        
        query = ("SELECT SUM(number) AS Total  FROM Commodity WHERE WarehouseName='%s'"%(Warehouse.name))
        sting.cursor.execute(query)
        results = sting.cursor.fetchone()  
        r=str(results)
        removed = r.replace("(", "")
        removed2 = removed.replace(", )", "")
        print str(removed2)
   
     
        
        sting.connection.commit()
        
    def showAllCommodity(self,Warehouse):
        query=("SELECT CommodityName FROM Commodity WHERE WarehouseName='%s' "
                                      %(Warehouse.name))
        sting.cursor.execute(query)
        results = sting.cursor.fetchall()
        for row in results:
            r=str(row)
            removed = r.replace("u'", "")
            removed2 = removed.replace("'", "")
            print str(removed2)
        
    def checkNumOfCommodity(self,Commodity):
        query=("SELECT number FROM Commodity WHERE CommodityName='%s' and Type='%s' and price='%s'"%(Commodity.name,Commodity.Type, Commodity.price))
        sting.cursor.execute(query)
        results = sting.cursor.fetchone()  
        r=str(results)
        removed = r.replace("(", "")
        removed2 = removed.replace(", )", "")
        print str(removed2)
    
    def showSpecificationCommodity(self, Commodity,Warehouse):
        query=("SELECT * FROM Commodity WHERE WarehouseName='%s' "
                                        %(Warehouse.name))
        sting.cursor.execute(query)
        results = sting.cursor.fetchall()
        for row in results:
            r=str(row)
            removed = r.replace("u'", "")
            removed2 = removed.replace("'", "")
            print str(removed2)
        

    def getName(self,Commodity):
        return Commodity.name        
        
    def getType(self,Commodity):
        return Commodity.Type
    
    def getNumber(self,Commodity):
        return Commodity.number
    
    def getPrice(self,Commodity):
        return Commodity.price
    
      
 #showSpecificationCommodity and showAllCommodity not   
        
        
        
        
        
        
        
