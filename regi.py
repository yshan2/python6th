from redis import StrictRedis

sr = StrictRedis()

while True:
	n = input('1,inser ; 2,look up ; 3, del ; 4, modify ')

	if n == '1':
		m = input('name? ')
		p = input('info? ')
		p2 = sr.get(m)
		if p2 is None:
			sr.set(m,p)
			print('done')
		else:
			print('already existed.')

	elif n == '2':
		m = input('name? ')
		r = sr.get(m)
		if r is None:
			print('not existed. ')
			continue
		print(r.decode())

	elif n == '3':
		m = input('name? ')
		if sr.get(m) is not None:
			sr.delete(m)
			print('done')
		else:
			print('not found.')

	elif n == '4':
		m = input('name? ')
		p = input('info? ')
		if sr.get(m) is not None:
			sr.set(m,p)
			print('done.')
		else:
			print('not exist.')

	else:
		print('you idiot. ')


