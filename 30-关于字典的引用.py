def keng():
	L = []
	dic = {'num':0}
	for i in range(10):
		dic['num'] = i
		L.append(dic)
	print(L)

# 输出为 [{'num':9}, {'num':9},.......], 列表内全是{'num':9}
# 解析

# 在第一次添加字典时, 将dic添加到列表中, 实际添加的是字典的引用, 
# 之后每次修改dic['num']的值时都会对应的将列表中已经添加的dic修改
# 所有最后一次遍历的时候将字典的num改为9, 列表内所有的字典num值也都改为9了