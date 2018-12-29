# -*- coding: utf-8 -*-
'''
@File  : serializers.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/26 0026 9:33
'''
# from django.contrib.auth.models import User,Group
from rest_framework import serializers
from api.models import User,Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('url','name')
