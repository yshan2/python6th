def src(l,n,s=0):
	e = len(l)-1
	if l[e] == n:
		return e
	elif l[0] == n:
		return 0
	return srch(l,s+1,e-1,n)

def srch(l,s,e,n):
	# if len(l)<1:
	# 	print('not found. ')
	# 	return -1
	m = (e-s)//2 + s
	a = l[m]
	if n == l[e]:
		return e
	elif n == l[s]:
		return s
	elif n>a:
		if n<l[e]:
			s2 = m  + 1
			return srch(l,s2,e,n)
		else:
			e2 = m  - 1
			return srch(l,s,e2,n)
	elif n == a:
		return m
	elif n<a:
		e2 = m - 1
		return srch(l,s,e2,n)
	# elif len(l)<3:
	# 	print('not found. ')
	# 	return -1

l = [17,18,19,0,1,2,6]
print(l)
print(src(l,11))


