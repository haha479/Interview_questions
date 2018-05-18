def func(*args):
	ax = 0
	
	def func_in():
		nonlocal ax
		for n in args:
			ax = ax + n
		return ax

	return func_in

a = func(1,2,3,4)
print(a())