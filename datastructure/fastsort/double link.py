class doubleChain():
	def __init__(self):
		self.__head = None
		self.__length = 0

	def is_empty(self):
		if self.__head is None:
			return True
		else:
			return False
	# 链表是否为空

	def length(self):
	# 链表长度
		return self.__length

	def travel(self):
	# 遍历链表
		n = self.__head
		while n is not None:
			print(n.value, end= ', ')
			n = n.next
		print('done')

	def add(self,item):
	# 链表头部添加
		n = node(item)
		if self.__head is None:
			self.__head = n
		else:
			i = self.__head
			i.pre = n
			self.__head = n
			n.next = i
		self.__length += 1

	def append(self,item):
	# 链表尾部添加
		if self.__head is not None:
			cur = self.__head
			n = node(item)
			while cur.next is not None:
				cur = cur.next
			cur.next = n
			n.pre = cur
		else:
			self.add(item)
		self.__length += 1

	def insert(self,pos,item):
	# 指定位置添加
		cur = self.__head
		n = node(item)
		if pos > self.length():
			self.append(item)
		elif pos < 2:
			self.add(item)
		else:
			for i in range(pos-1):
				cur = cur.next
			n.next = cur
			cur.pre.next = n
			cur.pre = n
		self.__length += 1

	def	remove(self,item):
		n = self.__head
		while n is not None:
			if n.value == item:
				n.pre.next = n.next
				n.next.pre = n.pre
				self.__length -= 1
				break
			n = n.next
		else:
			print('not found.')
		print('done remove.')

	# 删除节点
	def search(self,item):
	# 查找节点是否存在
		n = self.__head
		while n is not None:
			if n.value == item:
				print('found.')
				break
			n = n.next
		else:
			print('not found search.')

class node():
	def __init__(self,item):
		self.next = None
		self.pre = None
		self.value = item

l = doubleChain()
print(l.is_empty())
l.add(1)
l.add(2)
l.append(3)
l.travel()
print(l.is_empty())
print(l.length())
l.add(4)
print(l.length())
l.add(5)
print(l.length())
l.add(6)
print(l.length())
l.append(7)
print(l.length())
l.append(8)
print(l.length())
l.travel()
l.search(4)
l.remove(1)
print(l.length())
l.travel()
l.insert(5,10)
print(l.length())
l.travel()
print(l.length())
l.search(9)
l.search(10)










