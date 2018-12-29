# -*- coding: utf-8 -*-
'''
@File  : mysql_action.py.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/27 0027 9:18
'''
from pymysql import connect
import yaml

class DB():
    def __init__(self):
        print("connect db....")

        self.conn=connect(
            host='cdb-lsyn7ojl.gz.tencentcdb.com',
            user='root',
            password='306359211xxx',
            db='django_restful',
            port=10078,
        )
    def clear(self,tablename):
        print('clear db ...')
        clear_sql='truncate '+tablename+';'
        with self.conn.cursor() as cursor:
            # cursor.execute('set foreign_key_ckecks=0;')
            cursor.execute(clear_sql)
        self.conn.commit()

    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key]="'"+str(table_data[key])+"'"
        key=','.join(table_data.keys())
        value=','.join(table_data.values())
        print(key)
        print(value)
        insert_sql='insert into '+table_name+'('+key+')'+' values'+'('+value+');'
        print(insert_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()

    def init_data(self,datas):
        print('init data..')
        for table,data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table,d)
        self.close()


    def close(self):
        print("close db...")
        self.conn.close()
if __name__ == '__main__':
    db=DB()
    # db.clear('api_user')
    # user_data={'id':'1','username':"xiaowang",'email':'3123@qq.com','groups':'tester1'}
    # db.insert('api_user',user_data)
    #
    # db.close()
    f=open('datas','r')
    datas=yaml.load(f)
    f.close()
    db.init_data(datas)