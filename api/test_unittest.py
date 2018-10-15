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

# class UserTest(unittest.TestCase):
#     def setUp(self):
#         self.base_url='http://127.0.0.1:8000/users'
#         self.auth=('51zxw','51zxw20182018')
    #
    # def test_get_user(self):
    #     r=requests.get(self.base_url+'/1/',auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['username'],'51zxw')
    #     self.assertEqual(result['email'],'51zxw@163.com')
    #
    #
    # def test_add_user(self):
    #     from_data={'username':'Tom','email':'tom@124.com','groups':'http://127.0.0.1:8000/groups/1/'}
    #     r=requests.post(self.base_url+'/',data=from_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['username'],'Tom')
    #     self.assertEqual(result['email'],'tom@124.com')

    # def test_update_user(self):
    #     from_data={'email':'tom2018@126.com'}
    #     r=requests.patch(self.base_url+'/4/',data=from_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['email'],'tom2018@126.com')


    # def test_delete_user(self):
    #     r=requests.delete(self.base_url+'/4',auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)
    #
    # def test_no_auth(self):
    #
    #     r=requests.get(self.base_url)
    #     result=r.json()
    #
    #     self.assertEqual(result['detail'],'Authentication credentials were not provided.')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('51zxw', '51zxw20182018')
        #
    # def test_get_group(self):
    #     r=requests.get(self.base_url+'/1/',auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Tester')

    # def test_add_group(self):
    #     from_data={'name':'Pm'}
    #     r=requests.post(self.base_url+'/',data=from_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Pm')

    # def test_update_group(self):
    #     from_data={'name':'Leader'}
    #     r=requests.patch(self.base_url+'/1/',data=from_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Leader')

    #
    # def test_delete_group(self):
    #     r=requests.delete(self.base_url+'/3',auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)

    def test_no_auth(self):

        r=requests.get(self.base_url)
        result=r.json()

        self.assertEqual(result['detail'],'Authentication credentials were not provided.')


if __name__ == '__main__':

    unittest.main()
