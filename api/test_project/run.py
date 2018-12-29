# -*- coding: utf-8 -*-
'''
@File  : run.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/27 0027 13:43
'''
import unittest
from BSTestRunner import BSTestRunner
import time,yaml
from mysql_action import DB

db=DB()
f=open('datas','r')
datas=yaml.load(f)
db.init_data(datas)
test_dir='./'
report_dir='./reports'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_django_restful.py')

now=time.strftime("%Y%m%d %H_%M_%H")
report_name=report_dir+'/'+now+'result.html'

with open(report_name,'wb')as fb:
    runner=BSTestRunner(stream=fb,title='django_restful_api test report',description='sample')
    runner.run(discover)

