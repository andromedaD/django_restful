# -*- coding: utf-8 -*-
'''
@File  : test.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/26 0026 14:43
'''
import unittest
import requests

class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'
        self.auth=('wangzhiben','123456')

    def test_get_groups(self):
        r=requests.get(self.base_url+'/1',auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Tester1')
        self.assertEqual(result['url'],'http://127.0.0.1:8000/groups/1/')

    # def test_add_groups(self):
    #     form_data={'name':'Tester3','url':'http://127.0.0.1:8000/groups/3/'}
    #     r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
    #     result=r.json()
    #     self.assertEqual(result['name'],'Tester3')
    #     self.assertEqual(result['url'],'http://127.0.0.1:8000/groups/3/')
    #
    # def test_upadte_groups(self):
    #     form_data={'name':'Tester1'}
    #     r=requests.patch(self.base_url+'/1/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Tester1')
    # def test_delete_groups(self):
    #     r=requests.delete(self.base_url+'/3/',auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)


