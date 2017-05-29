from conn1 import *
# from pymysql import *


class co():
	def __init__(self):
		self.c = conne()
		self.cur = self.c.cursor()
	# def connectDB(self):


	def inp(self):
		i = input('1 lookup, 2 add, 3, modify, 4, del, 5, ext \n')
		if i == '1':
			self.cur.execute('select id,name from students where isdelete = 0')
			return self.cur.fetchall()
		elif i == '2':
			self.named()
			print(self.name)
			q= self.cur.execute('insert into students(name) VALUES(%s);',[self.name])
			return '%i row is effected. '%q
		elif i == '3':
			self.idd()
			self.named()
			try:

				s = ('update students set name = %s where id = %s')
				para = [self.name,self.id]
				q = self.cur.execute(s,para)
				if q == 0:
					return 'nothing changed.'
				else:
					return '%i row is effected. '%q
			except Exception:
				print('you fail.')
				return ''
		elif i == '4':
			cc = input('the id? ')
			q = self.cur.execute('update students set isdelete = 1 where id = %s ',[cc])
			if q == 0:
				return 'nothing changed.'
			else:
				return '%i row is effected. ' % q
		elif i == '5':
			return 'bye bye'
		else:
			print('fail. because of you. ')
			return ''


	def idd(self):
		self.id = input('id: ')

	def named(self):
		self.name = input('name: ')


def main():
	# print('x')
	con = co()
	print(con)
	print(con.c)
	c = con.c
	cur = con.cur

	# pa = para()
	# try:
	while True:
		x=con.inp()

		# cur.execute(x)
		print(x)
		if x == 'bye bye':
			break
		c.commit()

	# except Exception as e:
	# 	print(e)
	# 	c.rollback()
	# finally:
	c.close()


# print('y')
if __name__ == '__main__':
	main()
