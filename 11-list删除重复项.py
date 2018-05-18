list1 = [1,1,2,3,3,4,6,6,0]

# 使用集合去重
# a = set(list1)
# list2 = list(a)
# print(str(list2))

list2 = []

for i in list1:
	if i in list2:
		continue
	list2.append(i)

print(list2)
