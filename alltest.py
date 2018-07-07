# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 10:53:48 2018

@author: asus
"""

import sys
sys.path.append(r"C:\Users\asus\Desktop\warehouseSystem\Model")
sys.path.append(r"C:\Users\asus\Desktop\warehouseSystem\Controller")
from pyodbc import *
from Warehouse import Warehouse
from Commodity import Commodity
from Company import Company
from Manager import Manager
from OrderDetail import OrderDetail
from OrderAction import OrderAction
from ManagerAction import ManagerAction
import pandas as pd
from CommodityAction import CommodityAction
from Settings import Setting
sting = Setting()


print " -------add Commodity to database-------"
"""
for i in range(1,5):
    Com = Commodity('refrigerator'+str(i) ,'E13'+str(i) ,25+i ,'4000000'+str(i))
    Wer = Warehouse('warehouse1','100')
    
    commodity_obj = CommodityAction()
    commodity_obj.addCommodity(Com,Wer)

print "--------reduce commidity -------------"

for i in range(2,5):
    Com = Commodity('refrigerator'+str(i) ,'E13'+str(i) ,25+i ,'4000000'+str(i))
    Wer = Warehouse('warehouse1','100')
    commodity_obj = CommodityAction()
    commodity_obj.reduceCommodity(Com,2,Wer)
    """
print "----------------delete commidity------------------- "
for i in range(1,5):
    Com = Commodity('refrigerator'+str(i) ,'E13'+str(i) ,25+i ,'4000000'+str(i))
    Wer = Warehouse('warehouse1','100')
    commodity_obj = CommodityAction()
    commodity_obj.delCommodity(Com,Wer)

#-----------------------------
    """
Wer = Warehouse('warehouse1','100')
commodity_obj = CommodityAction()
commodity_obj.getTotalNumOfCommodity(Wer)

 
#---------------------createCompany-----------------------------  
for i in range(2,5):  
    comp=Company('company'+str(i),'company'+str(i)+'@gmail.com','2234124'+str(i),'tehran')
    company_obj = CompanyAction()
    company_obj.createCompany(comp)
 
#--------------------signup_Manager-----------------------------
 
man=Manager('admin','12345','manager@gmail.com') 
Manager_obj=ManagerAction()
Manager_obj.signUp(man)


#------------------add-warehouse--------------------------------
man=Manager('admin','12345','manager@gmail.com') 
comp=Company('company1','company1@gmail.com','22341241','tehran')
Wer = Warehouse('warehouse1','100')
Manager_obj=ManagerAction()
Manager_obj.addWarehouse(man,Wer,comp)

#--------------------del-warehouse----------------------------------
comp=Company('company1','company1@gmail.com','22341241','tehran')
Wer = Warehouse('warehouse1','100')
Manager_obj=ManagerAction()
Manager_obj.delWarehouse(Wer,comp)

#--------------------Commodity-Order---------------------------------
comp=Company('company1','company1@gmail.com','22341241','tehran')
order=OrderDetail(25,'97/1/1','2',comp)
Wer = Warehouse('warehouse1','100')
Com = Commodity('refrigerator1' ,'E132' ,26,'4000001')
Order_obj=OrderAction()
Order_obj.orderCommodity(order,Com,Wer,comp)
"""













      
