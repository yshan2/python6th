def fastsort(lst,start,end):
	if end - start < 2:
		return
	# i = start + 1
	left = start
	right = end
	while left < right:

		while left < right and lst[left] <= lst[start]:
			left += 1
		while left < right and lst[right] > lst[start]:
			right -= 1
		if lst[left] <= lst[start]:
			lst[left],lst[start] = lst[start],lst[left]
		else:
			lst[left],lst[right] = lst[right],lst[left]
	lst[start],lst[left-1] = lst[left-1],lst[start]

	fastsort(lst,start,left-2)
	fastsort(lst,left,end)

# l = [17, 20, 17]
l = [54,226,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20]
print(l)
fastsort(l,0,len(l)-1)
print(l)



