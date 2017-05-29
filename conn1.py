from pymysql import *

def conne(host='localhost', user='root', password="123",
                 database='python', port=3306, charset='utf8'):
	x = connect(host=host,user=user,password=password,database=database,port=port,charset=charset)
	return x