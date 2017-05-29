def comb(l):
	if len(l) >1:
		a = l[0:len(l)//2]
		b = l[len(l)//2:]

		a = comb(a)
		b = comb(b)

		i = 0
		j = 0
		s = []
		print(a)
		print(b)
		while i<len(a) and j<len(b):
			if a[i]<= b[j]:
				s.append(a[i])
				i+=1
			else:
				s.append(b[j])
				j+=1
		s.extend(a[i:])
		s.extend(b[j:])
		return s
	else:
		return l

l = [54, 226, 93, 17, 77, 31, 44, 55, 20, 54, 26, 93, 17, 77, 31, 44, 55]
print(l)
print()
a = comb(l)
print(a)






