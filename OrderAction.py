# -*- coding: utf-8 -*-
"""
Created on Fri Jun 08 16:19:32 2018

@author: Fatemeh
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
            SQLCommand = ("INSERT INTO Order"
                      "(orderNumber, date, status, CommodityName ,Type ,number ,price ,ComapanyName,WarehouseName)"
                      " VALUES ('%d','%s','%s','%s','%s','%d','%s','%s','%s')"
                      %(self.getOrderNumber(OrderDetail),self.getDate(OrderDetail),'2',
                        Commodity.name,Commodity.Type,Commodity.number,Commodity.price, Company.name,Warehouse.name))
            
            sting.cursor.execute(SQLCommand)
            sting.connection.commit()
            
    def numberOfOrder(self, Commodity, Warehouse ,Company):
        orderNum = pd.read_sql("SELECT number FROM Order WHERE (CommodityName,CompanyName,WarehouseName)"
                               "VALUES('%s','%s','%s')"%(Commodity.name,Company.name,Warehouse.name))
        return orderNum
    
    def checkStatusOrder(self,OrderDetail):
        status = pd.read_sql("SELECT status FROM Warehouse WHERE"
                     "(orderNumber, date)"
                     "VALUES ('%d','%s')"%
                     (self.getOrderNumber(OrderDetail),self.getDate(OrderDetail)))
        return status
    """       
    def update(self,Commodity,OrderDetail,Warehouse):
        numOfLost = self.getOrderNumber(Commodity, Warehouse, OrderDetail.asker)
        CommodityAction.reduceCommodity(self,Commodity,numOfLost,Warehouse)
            SQLCommand = ("UPDATE Warehouse SET WarehouseName=%s,Capacity=%s WHERE WarehouseName=%s, Capacity=%s"
                     %(newName,newCapacity,Warehouse.name,Warehouse.capacity))
    """    
        
        
                              
                              
                              
                              
                              
   
    def getOrderNumber(self,OrderDetail):
        return OrderDetail.orderNumber
    
    def getDate(self,OrderDetail):
        return OrderDetail.date
    
    def getStatus(self,OrderDetail):
        return OrderDetail.status
    
    
