# try:
# 	raise ValueError('something wrong')

# except ValueError as e:
# 	print('hahha')
# 	raise 

# class Context:
# 	def __enter__(self):
# 		print('enter')

# 	def __exit__(self):
# 		print('exit')

# with Context() as ctx:
# 	ctx.do_something()


# def say_hi(func):
# 	def wrapper(*args, **kwargs):
# 		print('Hi')
# 		ret = func(*args, **kwargs)
# 		print('Bye')
# 		return ret
# 	return wrapper

# def say_yo(func):
# 	def wrapper(*args, **kwargs):
# 		print('yo')
# 		return func(*args, **kwargs)

# 	return wrapper


# @say_hi
# @say_yo
# def func():
# 	print('rock_roll')

# func()

# def test():
# 	try:
# 		raise ValueError('something wrong')

# 	except ValueError as e:
# 		print('error occ')
# 		return 

# 	finally:
# 		print('done')

# test()


def dict_up(k,v,dic={}):
	dic[k] = v
	print(dic)

dict_up('one',1)
dict_up('two',2)
dict_up('three',3,{})













