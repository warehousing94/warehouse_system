# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 12:06:24 2018

@author: asus
"""
from pyodbc import *
import pandas as pd
class Setting():
    def __init__(self):
        self.connection = connect(r'Driver={SQL Server};Server=DESKTOP-T60JE22\MYSQLSERVER;Database=Warehouse;Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()
        self.connection.commit()
