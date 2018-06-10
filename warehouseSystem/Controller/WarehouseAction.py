# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 16:06:42 2018

@author: Fatemeh
"""

class WarehouseAction(object):
    
    def getId(self,warehouse):
        return warehouse.id
    
    def getName(self,warehouse):
        return warehouse.name
    
    def getCapacity(self,warehouse):
        return warehouse.capacity
    
