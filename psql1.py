# from pymysql import *
import conn1

if __name__ == '__main__':
	try:

		conn = conn1.conne()
		cur = conn.cursor()
		# sql = "insert into students(NAME) VALUE (%s)"
		# para = [input('value? ')]

		# cur.execute(sql,para)
		# print(cur.description)

		# conn.commit()
		sql2='select name,gender from students where isdelete = 0 and gender =0'
		cur.execute(sql2)
		print(cur.description)
		a = cur.fetchall()
		print(a)



	except Exception as e:
		print(e)
		conn.rollback()

	finally:
		conn.close()





