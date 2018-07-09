# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:16:17 2018

@author: admin
"""

import sys
sys.path.append(r"D:\uni\term10\software\warehouse_system-master\warehouse_system-master\phaze2\Model")
from pyodbc import *
import pandas as pd
from Settings import Setting
sting = Setting()
from Request import Request
from Company import Company
from Commodity import Commodity
from Warehouse import Warehouse
from CommodityAction import CommodityAction


        
class RequestAction(object):
    
    def requestCommodity(self ,Request,Commodity,Warehouse,Company):        #create request by warehouse to company
            SQLCommand = ("INSERT INTO Request"
                      "(requestID, date, status, CommodityName, Type, number, price, WarehouseName, ComapanyName)"
                      " VALUES ('%d','%s','%s','%s','%s','%d','%s','%s','%s')"
                      %(Request.requestID,Request.date,'2',Commodity.name,Commodity.Type,Request.number,Commodity.price,Warehouse.name,Company.name ))
            sting.cursor.execute(SQLCommand)
            sting.connection.commit()


            
    def acceptRequeststatus(self,Request):        #status = 1 and add commodity number
        SQLCommand= ("UPDATE Request SET status='1' WHERE requestID='%d'"%(Request.requestID) )
        sting.cursor.execute(SQLCommand)
        self.acceptRequestNumber(Request)
        sting.connection.commit()
        
                
            
    def acceptRequestNumber(self,Request):         #add commodity to warehouse by request

            SQLCommand = ("UPDATE Commodity SET number=number +(SELECT number FROM Request WHERE  requestID = '%d')"            
                            "WHERE( CommodityName = (SELECT CommodityName FROM Request WHERE  requestID = '%d') and WarehouseName=(SELECT WarehouseName FROM Request WHERE  requestID = '%d') and Type=(SELECT Type FROM Request WHERE  requestID = '%d'))"
                     %(Request.requestID,Request.requestID,Request.requestID,Request.requestID))
            sting.cursor.execute(SQLCommand)
            sting.connection.commit()
    

        
    def checkNumber(self,Warehouse):      #say cmmodity that in few number
        checkNumber=("SELECT CommodityName , number FROM Commodity WHERE WarehouseName='%s'"  %(Warehouse.name))
        sting.cursor.execute(checkNumber)
        result = sting.cursor.fetchall()       
        result = [x for x in result]
        for i in range(0,len(result)):            
            if (result[i][1]<50):
                print "Commodity",result[i][0],":",result[i][1], "number,please request commodity"
            else:
                print "Commodity",result[i][0],":",result[i][1], "number, It's OK!"
        sting.connection.commit()
          
    def checkStatusRequest(self,Request):
        
        status =("SELECT status FROM Request WHERE requestID='%d'"%(Request.requestID))       
        sting.cursor.execute(status)
        results = sting.cursor.fetchone()  
        Print(results)
        sting.connection.commit()


        
    def getNumberOfRequest(self,Request):
        
        number = ("SELECT number FROM Request WHERE requestID='%d'"%(Request.requestID))
        sting.cursor.execute(number)
        result = sting.cursor.fetchone()
        Print(result)
        sting.connection.commit()

 
    
    def getRequestDate(self,Request):
        
        date = ("SELECT date FROM Request WHERE requestID='%d'"%(Request.requestID))
        sting.cursor.execute(date)
        result = sting.cursor.fetchone()
        Print(result)
        sting.connection.commit()

    

#_____________________________________
def Print(results):
        r=str(results)
        removed = r.replace("(", "")
        removed2 = removed.replace(", )", "")
        print str(removed2)       
#_____________________________________
    