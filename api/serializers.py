#!/usr/bin/python  
#coding:utf-8  

""" 
@author: DengKele
@contact: 891786333@qq.com 
@software: PyCharm 
@file: serializers.py 
@time: 2018/9/13 17:41 
"""  
# from django.contrib.auth.models import User,Group
from  rest_framework import serializers
from api.models import User,Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('url','name')



