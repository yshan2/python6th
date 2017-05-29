def least(l,n):
	if n < 1:
		return
	i = 0
	j = i
	for i in range(len(l)):
		if l[j] > l[i]:
			j = i
	print(l[j])
	l = l[:j]+l[j+1:]
	least(l,n-1)

def least2(l2,n):
	l = list(tuple(l2))
	# l.append(3)
	# print(l)
	# print(l2)
	for j in range(len(l)-1):
		for i in range(len(l)-j-1):
			if l[i] > l[i+1]:
				l[i],l[i+1] = l[i+1],l[i]
	print(l)
	for p in range(n):
		print(l[p])

s = [54, 226, 93, 17, 77, 31, 44, 55, 20, 54, 26, 93, 17, 77, 31, 44, 55, 20]
print(s)
least(s,2)

least2(s,3)




