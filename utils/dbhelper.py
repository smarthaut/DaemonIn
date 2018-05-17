#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 11:10
# @Author  : huanghe
# @Site    : 
# @File    : dbhelper.py
# @Software: PyCharm
import pymongo
from utils.config import Config

class Mongodb:
    def __init__(self):
        cf = Config().get('mongodb')
        self.host = cf.get('host')
        self.port = cf.get('port')
        self.user = cf.get('user')
        self.password = cf.get('password')
        try:
            self.client = pymongo.MongoClient(self.host, port=int(self.port))
        except:
            print('数据库连接失败')

    def getConnection(self, table_name, connection_name):
        db = self.client.get_database(table_name)
        connection = db.get_collection(connection_name)
        return connection