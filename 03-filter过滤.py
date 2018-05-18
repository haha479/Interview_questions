# encoding:utf-8
# filter函数，指定一个序列中的每一项执行一个函数,该函数必须返回一个布尔值,
# 在python3中filter函数得到的是一个迭代器
a = [1,2,3,4,5,6,7]
b = filter(lambda x : x > 5,a)

for item in b:
	print(item)

# def test(x):
	# 返回的是一个布尔值
# 	return x % 2 == 1


# for item in filter(test, a):
# 	print(item)
