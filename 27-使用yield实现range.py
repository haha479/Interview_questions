

def range_func(num):
	for i in range(num):
		yield i

for i in range_func(10)	:
	print(i)
