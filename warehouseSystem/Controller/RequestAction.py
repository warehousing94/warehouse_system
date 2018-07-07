# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:16:17 2018

@author: admin
"""

import sys
#sys.path.append(r"D:\uni\term10\software\warehouse_system-master\warehouse_system-master\warehouseSystem\Model")
import pandas as pd
from Request import Request
from Company import Company
from Commodity import Commodity
from Warehouse import Warehouse
from CommodityAction import CommodityAction

class RequestAction(object):
    def requestCommodity(self ,Request,Commodity ,Company ,Warehouse):
            SQLCommand = ("INSERT INTO Request"
                      "(requestID, date, status, CommodityName, Type, number, price, ComapanyName,WarehouseName)"
                      " VALUES ('%d','%s','%s','%s','%s','%d','%s','%s','%s')"
                      %(Request.requestID,Request.date,'2',Commodity.name,Commodity.Type,Request.number,Commodity.price, Company.name ,Warehouse.name))
            sting.cursor.execute(SQLCommand)
            sting.connection.commit()
#    def numberOfRequest(self, Commodity, Warehouse ,Company):
#        RequestNum = pd.read_sql("SELECT number FROM Request WHERE (CommodityName,CompanyName,WarehouseName)"
#                               "VALUES('%s','%s','%s')"%(Commodity.name,Company.name,Warehouse.name))
#        return RequestNum
    
    def checkStatusRequest(self,Request):
        status = pd.read_sql("SELECT status FROM Request WHERE"
                     "(requestID)"
                     "VALUES ('%d')"%
                     (Request.requestID))
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
        return status
        
    
    def update(self,Commodity,Request,Company):
       # numOfAdd = self.getRequestNumber(Commodity, Warehouse, Request.asker)
        #CommodityAction.reduceCommodity(self,Commodity,numOfLost,Warehouse)
            SQLCommand = ("UPDATE Commodity SET Commodity.number=Commodity.number + (SELECT Request.number FROM Request WHERE  requestID = '%d')"
                            "FROM Request"
                            "WHERE( Commodity.name = '%s' AND Commodity.Type = '%s' )"
                     %(Request.requestID,Commodity.name ,Commodity.Type ))
            sting.cursor.execute(SQLCommand)
            sting.connection.commit()
    
        
    def getRequestNumber(self,Request):
        
        return Request.number
    
    def getRequestDate(self,Request):
        return Request.date
    
    def getRequestStatus(self,Request):
        return Request.status
    
    def acceptRequest(self,Request):
        SQLCommand= ("UPDATE Request SET status='1' WHERE requestID='%d'"%(Request.requestID) )
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
        
    def checkNumber(self,Commodity ,Warehouse):
        checkNumber=pd.read_sql("SELECT Commodity.number FROM Commodity WHERE Warehouse.name='%s'" %(Warehouse.name))
        
        if (checkNumber <50):
            self.requestCommodity(Request,Commodity ,Company)
        
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
        
        
        
