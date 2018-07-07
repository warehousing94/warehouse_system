# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:10:05 2018

@author: admin
"""

import sys
sys.path.append(r"C:\Users\asus\Desktop\warehouseSystem\Model")
from pyodbc import *
from Warehouse import Warehouse
from Company import Company

from Settings import Setting
sting = Setting()

class CompanyAction(object):


    def createCompany(self,Company):
        SQLCommand = ("INSERT INTO Company "
                      "(CompanyName, Email,phone,address)"
                      "VALUES ('%s','%s','%s','%s')"%
                      (Company.name,Company.email,Company.phone,Company.address))
        sting.cursor.execute(SQLCommand)
        sting.connection.commit()


  
