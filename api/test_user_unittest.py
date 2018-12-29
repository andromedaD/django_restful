# -*- coding: utf-8 -*-
'''
@File  : test_unittest.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/26 0026 14:12
'''
import unittest
import requests
class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('wangzhiben','123456')

    def test_get_user(self):
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'wangzhiben')
        self.assertEqual(result['email'],'321@qq.com')
    #
    # def test_add_user(self):
    #     form_data={'username':'ganggang','email':'33@qq.com','groups':'http://127.0.0.1:8000/groups/1/'}
    #     r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['username'],'ganggang')
    #     self.assertEqual(result['email'],'33@qq.com')

    # def test_update_user(self):
    #     form_data={'email':'343@qq.com'}
    #     r=requests.patch(self.base_url+'/5/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['email'],'343@qq.com')

    # def test_delete_user(self):
    #     r=requests.delete(self.base_url+'/5/',auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)

    def test_no_auth(self):
        r=requests.get(self.base_url)
        result=r.json()
        self.assertEqual(result['detail'],'Authentication credentials were not provided.')


