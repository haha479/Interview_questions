# 等腰
def Isosceles():
	num = int(input('input num:'))
	for i in range(0,num+1):
		for y in range(0, num-i):
			print(" ", end="")
		print("* " * i)

# 直角
def right_angle():
	num = int(input('input num:'))
	for i in range(0, num+1):
		for y in range(i):
			print('* ',end="")
		print('')
right_angle()
