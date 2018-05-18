# def main(*args,**kwargs):
# 	for i in args:
# 		print('args->:',i)	

# 	for item in kwargs.items():
# 		print('kwargs->:',item)

# A = [1,2,3,4,5]
# B = {'name':'haha','age':18}

# main(A,B)


def main(*args,**kwargs):
	for i in args:
		print('args->:',i)	

	for item in kwargs.items():
		print('kwargs->:',item)

A = [1,2,3,4,5]
B = {'name':'haha','age':18}

main(*A,**B)