class node:
	def __init__(self,v):
		self.next = None
		self.value = v
		self.pre= None

	# def __str__(self):
	# 	return self.value


class singleChain:
	def __init__(self):
		self.__head = None
		self.__count = 0
		# self.__next = None

	def add(self,v):
		a = node(v)
		a.next = self.__head
		self.__head = a
		self.__count += 1

	def addtail(self,v):
		a = node(v)
		if self.__head is not None:
			cur = self.__head
			while cur.next is not None:
				cur = cur.next
			cur.next = a
		else:
			self.add(v)
		self.__count += 1

	def traval(self):
		if self.__head is not None:
			cur = self.__head
			print(cur.value,end=' ')
			while cur.next is not None:
				cur = cur.next
				print(cur.value,end=' ')
		print('  end.')

	def prt2(self):
		cur = self.__head
		pre = None
		stash = []
		while cur.next is not None:
			stash.append(cur)
			cur = cur.next
		stash.append(cur)
		while len(stash) > 0 :
			print(stash.pop().value,end=' ')
		print(' end.')

	def prt(self):
		cur = self.__head
		while cur.next is not None:
			cur.next.pre = cur
			cur = cur.next
		while cur.pre is not None:
			print(cur.value,end=' ')
			cur = cur.pre
		print(cur.value, end=' reverse end. \n')

	def revk(self,k):
		if k <= self.__count:
			cur = self.__head
			c = self.__count - k
			while c > 0:
				cur = cur.next
				c -= 1
			print(cur.value,end= ' as the reverse %d\'s\n' % k)
		else: print(self.__head.value, end= ' as the reverse %d\'s\n' % k)

	def revs(self):
		if self.__count > 0:
			cur = self.__head
			aft = cur.next
			pre = None
			cur.next = None
			while aft is not None:
				pre = cur
				cur = aft
				aft = aft.next
				cur.next = pre
			cur.next = pre
			self.__head = cur



x = singleChain()
x.revs()
x.add(1)
x.revs()
x.traval()
x.add(2)
x.traval()
x.addtail(4)
x.addtail(5)
x.traval()
x.revs()
x.traval()
x.addtail(6)
x.addtail(7)
x.add(8)
x.traval()
x.prt()
x.revk(3)
x.revk(5)
x.revk(9)
x.revs()
# x.prt()
x.traval()
x.prt2()





