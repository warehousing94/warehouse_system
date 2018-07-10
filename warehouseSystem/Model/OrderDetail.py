# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 18:27:36 2018

@author: Fatemeh
"""
from Status import Status
class OrderDetail(object):
    def __init__(self, orderNumber, date, Status,Warehose,Company):
        self.orderNumber = orderNumber
        self.date = date
        self.status = Status
        self.sender = Warehose
        self.reciever = Company

        
