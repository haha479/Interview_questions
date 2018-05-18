def foo(count):
	a,b = 0,1

	while a < count:
		yield a
		a,b = b,a+b

for i in foo(10):
	print(i)