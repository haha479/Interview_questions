st = '  hello word '
def trim(st):
	if st[:1] !=' ' and st[-1:] !=' ':
		return st
	elif st[:1] == ' ':
		return trim(st[1:])
	else:
		return trim(st[:-1])

# print(trim(st))

# 求出指定列表中的最大和最小值
lis = [2,3,4,5,6,7,8]
max_num = 0
min_num = 5

def max_min(max_num, min_num, lis):

	for num in lis:
		if num > max_num:
			max_num = num
		if num < min_num:
			min_num = num

	return min_num,max_num

print(max_min(max_num, min_num, lis))