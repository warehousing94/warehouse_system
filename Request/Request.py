# -*- coding: utf-8 -*-
"""
Created on Sun Jun 1 11:34:16 2018

@author: R.S
"""

from Status import Status
class Request(object):
    def __init__(self, requestID, date, Status):
        self.requestID = requestID
        self.date = date
        self.status = Status
        self.asker = Company()
   

        