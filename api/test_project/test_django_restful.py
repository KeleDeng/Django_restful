#!/usr/bin/python
#coding:utf-8

"""
@author: DengKele
@contact: 891786333@qq.com
@software: PyCharm
@file: test_unittest.py
@time: 2018/9/13 22:40
"""
import requests
import unittest
from mysql_action import DB
import yaml
import logging
#
class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('2018zxw','zxw20182018')
    #
    def test_001_get_user(self):
        logging.info('test_001_get_user')
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'sutune')
        self.assertEqual(result['email'],'sutune@163.com;')
    #
    #
    def test_002_add_user(self):
        logging.info('test_002_add_user')
        from_data={'username':'Tom','email':'tom@124.com','groups':'http://127.0.0.1:8000/groups/1/'}
        r=requests.post(self.base_url+'/',data=from_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'Tom')
        self.assertEqual(result['email'],'tom@124.com')

    def test__003_update_user(self):
        logging.info('test__003_update_user')
        from_data={'email':'sutune2018@126.com'}
        r=requests.patch(self.base_url+'/1/',data=from_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['email'],'sutune2018@126.com')


    def test_004_delete_user(self):
        logging.info('test_004_delete_user')
        r=requests.delete(self.base_url+'/2/',auth=self.auth)

        self.assertEqual(r.status_code,204)
    #
    def test_005_no_auth(self):
        logging.info('test_005_no_auth')
        r=requests.get(self.base_url)
        result=r.json()

        self.assertEqual(result['detail'],'Authentication credentials were not provided.')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('2018zxw', 'zxw20182018')
        #
    def test_001_get_group(self):
        logging.info('test_001_get_group')
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Developer')

    def test_002_add_group(self):
        logging.info('test_002_add_group')
        from_data={'name':'Pm'}
        r=requests.post(self.base_url+'/',data=from_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Pm')

    def test_003_update_group(self):
        logging.info('test_003_update_group')
        from_data={'name':'Leader'}
        r=requests.patch(self.base_url+'/2/',data=from_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Leader')

    #

    def test_004_delete_group(self):
        logging.info('test_004_delete_group')
        r=requests.delete(self.base_url+'/1/',auth=self.auth)

        self.assertEqual(r.status_code,204)

    def test_005_no_auth(self):
        logging.info('test_005_no_auth')
        r=requests.get(self.base_url)
        result=r.json()
        self.assertEqual(result['detail'],'Authentication credentials were not provided.')


# """调用mysql_action的DB()方法"""

    db=DB()
    f=open('datas.yaml','r')
    datas=yaml.load(f)
    db.init_data(datas)

if __name__ == '__main__':
    unittest.main()