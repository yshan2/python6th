from pymongo import *
from pymysql import *

uname = input('name: ')
sql = 'select student.name,class.name from student inner JOIN class on student.clsid = class.id where student.name = %s'
para = [uname]

try:
	client = MongoClient('localhost', 27017)
	db = client.test

	result = db.student.find_one({'uname': uname})
	# print(result)
	if result is None:
		try:
			conn = connect(host = 'localhost',port = 3306,charset = 'utf8', database = 'test2' ,user = 'root', password = '123')
			cur = conn.cursor()
			re = cur.execute(sql,para)
			p = cur.fetchone()

			# print(re)
			if re == 0:
				print('not found. ')
			else:
				print('found him in class '+p[1])
				clsid = p[1]

				db.student.insert_one({'uname': uname, 'clsid': clsid})
				print('added in mongo.')
		except Exception as e:
			print(e)
		finally:
			conn.close()

	else:
		# print(result)
		print('found him in class '+ result['clsid']+' from mongo')
except Exception as e:
	print(e)
#
# finally:
#












