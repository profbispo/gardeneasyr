'''import MySQLdb

class ConMys:

        def __init__(self, query):
                self.query = query
                self.db = MySQLdb.connect(host='meuhost', user='usuario', passwd='senha', db='BD')
                self.cursor = self.db.cursor()
                self.cursor.execute(self.query)
                self.numrows = int(self.cursor.rowcount)
        def query_tudo(self):
                self.row = self.cursor.fetchall()
                return (self.row, self.numrows)
        def query_exato(self):
                self.row = self.cursor.fetchone()
                return (self.row, self.numrows)
'''
import mysql.connector
class ConMys:
        def __init__(self, query):
                self.query = query
                self.cnx = mysql.connector.connect(user='root', password='senha12',
                                                   host='127.0.0.1',
                                                   database='banco')
                self.cursor = self.cnx.cursor()
                self.cursor.execute(self.query)
                self.numrows = int(self.cursor.rowcount)

        def query_tudo(self):
                self.row = self.cursor.fetchall()
                self.cnx.close()
                return (self.row, self.numrows)

        def query_exato(self):
                self.row = self.cursor.fetchone()
                self.cnx.close()
                return (self.row, self.numrows)
