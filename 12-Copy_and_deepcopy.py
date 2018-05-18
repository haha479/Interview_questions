import copy

list1 = [1,2,3,4,['a','b']]

list2 = list1

list3 = copy.copy(list1) # 浅拷贝
list4 = copy.deepcopy(list1) # 深拷贝

# 浅拷贝 : 复制了对象, 但对于对象中的元素,依然使用原始的引用
# 深拷贝 : 复制了对象,以及它里面所有元素,这样原对象中元素发生了改变都不关拷贝后的关系


# 修改原对象
list1.append(5)

# 修改原对象中的['a','b']列表
list1[4].append('c')

print('list1=',str(list1))

print('list2=',str(list2))
print('list3=',str(list3))
print('list4=',str(list4))


