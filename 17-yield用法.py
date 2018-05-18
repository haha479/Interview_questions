import os
import sys
# 斐波拉契数列
# def func(count):
# 	a,b = 0,1
# 	for i in range(count):
# 		a, b = b, a+b
# 		yield b
# 		print(b)

# a = func(20)
# next(a)
# next(a)
# next(a)

def func():
	for i in range(10):
		yield i
		print(i)

f = func()
next(f)
next(f)
next(f)


