from pymysql import *

def conn(host='localhost', port = 3306, charset = 'utf8', database = 'python',user = 'root', password ='123'):
	return connect(host = host,port = port,charset = charset, database = database ,user = user, password = password)