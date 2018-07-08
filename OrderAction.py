# -*- coding: utf-8 -*-
"""
Created on Fri Jun 08 16:19:32 2018

@author: maryam
"""
import sys
sys.path.append(r"C:\Users\asus\Desktop\warehouseSystem\Model")
import pandas as pd
from OrderDetail import OrderDetail
from Company import Company
from Commodity import Commodity
from Warehouse import Warehouse
from CommodityAction import CommodityAction

from Settings import Setting
sting = Setting()

class OrderAction(object):
    def orderCommodity(self ,OrderDetail ,Commodity ,Warehouse,Company):
        SQLCommand = ("INSERT INTO Table_1"
                      "(orderNumber, date, status, CommodityName ,Type ,number ,price ,CompanyName,WarehouseName)"
                      " VALUES ('%d','%s','%s','%s','%s','%d','%s','%s','%s')"
                      %(self.getOrderNumber(OrderDetail),self.getDate(OrderDetail),'2',
                        Commodity.name,Commodity.Type,Commodity.number,Commodity.price, Company.name,Warehouse.name))
        
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()
            
    def numberOfOrder(self, Commodity, Warehouse ,Company):
        query=("SELECT number FROM Table_1 WHERE CommodityName='%s' and CompanyName='%s' and WarehouseName='%s'"%(Commodity.name,Company.name,Warehouse.name))
        sting.cursor.execute(query)
        results = sting.cursor.fetchone()  
        r=str(results)
        removed = r.replace("(", "")
        removed2 = removed.replace(", )", "")
        print str(removed2)
        sting.connection.commit()
    def checkStatusOrder(self,OrderDetail):
        query=("SELECT status FROM Table_1 WHERE orderNumber=%d and date='%s'"%
                     (self.getOrderNumber(OrderDetail),self.getDate(OrderDetail)))
        sting.cursor.execute(query)
        results = sting.cursor.fetchone()  
        r=str(results)
        removed = r.replace("(u'", "")
        removed2 = removed.replace("', )", "")
        print str(removed2)
        
        sting.connection.commit()
                               
    def getOrderNumber(self,OrderDetail):
        return OrderDetail.orderNumber
    
    def getDate(self,OrderDetail):
        return OrderDetail.date
    
    def getStatus(self,OrderDetail):
        return OrderDetail.status
    
    
