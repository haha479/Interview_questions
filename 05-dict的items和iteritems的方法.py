# -*- coding:utf-8 -*-
dict1 = {'a':1,'b':2,'c':3}

# dict2 = {'d':4,'e':5,'f':6}

items = dict1.items()
# 返回的是一个列表
print('item对象',items)

iteritems = dict1.iteritems()
# 返回的是一个迭代器
print('iteritem对象',iteritems)
# for item in dict1.items():
# 	print(item)