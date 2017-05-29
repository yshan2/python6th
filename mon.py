from pymongo import *
from hashlib import sha1
from pymysql import *

def mysql_login(uname,upsd_s,db):
	sql = 'select upsd from user where name=%s'
	para = [uname]
	try:
		conn= connect(host='localhost',port=3306,database = 'python',user = 'root',password = '123',charset = 'utf8')
		cur = conn.cursor()
		cur.execute(sql,para)
		result = cur.fetchone()
		cur.close()
		print(result)
		print(upsd_s)
		if result is None:
			print('wrong name.')
		else:
			db.user.insert_one({'uname':uname,'upsd':upsd_s})
			if result[0]==upsd_s:
				print('success, mysql')
			else:
				print('wrong psd,mysql')
	except Exception as e:
		print(e)
	finally:
		conn.close()

def main():
	try:
		uname = input('name: ')
		upsd = input('password: ')

		s1 = sha1()
		s1.update(upsd.encode())
		upsd_s = s1.hexdigest()

		client = MongoClient('localhost',27017)
		db = client.py3
		result = db.user.find_one({'uname':uname})
		if result ==None:
			mysql_login(uname,upsd_s,db)

		else:
			if result['upsd']==upsd_s:
				print('sucess,mongo')
			else:
				print('wrong password,mongo')
		pass





	except Exception as e:
		print('fail as you did this : '+ e)


if __name__ == '__main__':
    main()
