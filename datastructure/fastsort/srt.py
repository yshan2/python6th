def sort(lst):
	l = len(lst)
	gap = l//2

	while gap>0:
		i = 1
		while i < l:
			while i-gap >= 0 and lst[i]<lst[i-gap]:
				lst[i],lst[i-gap] = lst[i-gap],lst[i]
				i -= 1
			i += 1
		gap = gap//2

a = [54,226,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20]
print(a)
sort(a)
print(a)





