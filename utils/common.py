#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 11:25
# @Author  : huanghe
# @Site    : 
# @File    : common.py
# @Software: PyCharm
import requests
import json
from utils.config import Config

class BaseHttp:

    def __init__(self,projectname):
        self.scheme = Config().get(projectname).get('scheme')
        self.host = Config().get(projectname).get('host')
        self.port = Config().get(projectname).get('port')
        self.timeout = Config().get(projectname).get('timeout')
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self,url):
        self.url = self.scheme + self.host + self.port + url

    def set_headers(self,header):
        self.headers = header

    def set_params(self,param):
        self.params = param

    def set_data(self,data):
        self.data = data

    def set_file(self,filename):
        if filename != '':
            file_path = 'D:/python/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(self.timeout))
            return response
        except TimeoutError:
            return None

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data, timeout=float(self.timeout))
            return response
        except TimeoutError:
            return None

    def post_file(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(self.timeout))
            return response
        except TimeoutError:
            return None
    def post_json(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
            return response
        except TimeoutError:
            return None

if __name__ =='__main__':
    basehttp = BaseHttp(projectname='adv')
    print(basehttp.host)


