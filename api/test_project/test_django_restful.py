# -*- coding: utf-8 -*-
'''
@File  : test_django_restful.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/27 0027 11:43
'''
from api.test_project.mysql_action import DB
import requests
import unittest
import yaml

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('wangzhiben','123456')

    def test_001_get_user(self):
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'xiaowang')
        self.assertEqual(result['email'],'3543@qq.com')

    def test_002_add_user(self):
        form_data={'username':'ganggang','email':'33@qq.com','groups':'http://127.0.0.1:8000/groups/1/'}
        r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'ganggang')
        self.assertEqual(result['email'],'33@qq.com')

    def test_003_update_user(self):
        form_data={'email':'343@qq.com'}
        r=requests.patch(self.base_url+'/1/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['email'],'343@qq.com')

    def test_004_delete_user(self):
        r=requests.delete(self.base_url+'/2/',auth=self.auth)

        self.assertEqual(r.status_code,204)

    def test_005_no_auth(self):
        r=requests.get(self.base_url)
        result=r.json()
        self.assertEqual(result['detail'],'Authentication credentials were not provided.')

class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'
        self.auth=('wangzhiben','123456')

    def test_006_get_groups(self):
        r=requests.get(self.base_url+'/1',auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Developer')
        self.assertEqual(result['url'],'http://127.0.0.1:8000/groups/1/')

    def test_007_add_groups(self):
        form_data={'name':'Tester3','url':'http://127.0.0.1:8000/groups/3/'}
        r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
        result=r.json()
        self.assertEqual(result['name'],'Tester3')
        self.assertEqual(result['url'],'http://127.0.0.1:8000/groups/3/')

    def test_008_upadte_groups(self):
        form_data={'name':'Tester1'}
        r=requests.patch(self.base_url+'/1/',data=form_data,auth=self.auth)
        result=r.json()
        self.assertEqual(result['name'],'Tester1')

    def test_009_delete_groups(self):
        r=requests.delete(self.base_url+'/3/',auth=self.auth)

        self.assertEqual(r.status_code,204)

if __name__ == '__main__':
    db=DB()
    f=open('datas','r')
    datas=yaml.load(f)
    db.init_data(datas)
    unittest.main()
