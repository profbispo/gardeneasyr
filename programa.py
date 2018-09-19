#coding: utf-8
import time
#import Tkinter
from connect.conf import APPNAME,parameters
from connect.mysqlPython import mysql_python

connect_mysql = mysql_python.MysqlPython(parameters["servidor"],
                                         parameters["userBanco"],
                                         parameters["senhaUserBanco"],
                                         parameters["banco"])


sql_query = 'select * from modules'

result = connect_mysql.select_advanced(sql_query)

print(result)


'''
sql_query = 'select * from contas'




print(result)

while (1==2):
    print(result)

    for x in result:
        print(x)
    time.sleep(2)

conditional_query =' true limit 2 '
result = connect_mysql.select('contas', None, 'Conta_ID')





from connect import sgbd

x = sgbd.ConMys("select * from contas")

print(x.query_tudo())

'''

result = connect_mysql.select_advanced(sql_query)

