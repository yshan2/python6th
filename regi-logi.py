from hashlib import sha1
from conn2 import *
from pymongo import *
from redis import StrictRedis

def sqlr(uname,upsd):
	con = conn(database='python')
	cur = con.cursor()

	sqlf = 'select name from user'
	re = cur.execute(sqlf)
	print(re)
	x = cur.fetchone()
	print(x)
	if uname in x:
		print('name existed. ')

	else:
		sql = 'insert into user(name,upsd) VALUES(%s,%s)'
		para = [uname,upsd]
		cur.execute(sql, para)
		con.commit()
	con.close()

def main():
	uname = input('name: ')
	upsd = input('password: ')

	sha = sha1()
	sha.update(upsd.encode())
	upsd_sha = sha.hexdigest()

	sr = StrictRedis()
	r = sr.get(uname)
	print(r)
	if r == None:
		sqlr(uname,upsd_sha)



	# sr = StrictRedis()
	# r = sr.set('uname',uname)
	# print(r)

# cli = MongoClient(host='localhost',port=27017)
# db = cli.test
# result = db.stu.update_one({'gender':True},{'$set':{'name':'aaaa'}})
# print(result)
# # for i in result:
# # 	print(i)


if __name__ == '__main__':
    main()









