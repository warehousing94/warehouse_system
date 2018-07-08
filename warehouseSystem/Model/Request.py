# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:11:49 2018

@author: admin
"""
from Commodity import Commodity
from Status import Status
from Manager import Manager
from Company import Company

class Request(object):
    def __init__(self, requestID, date, Status,number,Commodity,Manager,Company):
        self.requestID = requestID
        self.date = date
        self.status = Status
        self.number = number
        self.CommodityName = Commodity.name
        self.sender = Manager.username
        self.reciever = Company.name