# 给出一个列表和一个值, 如果列表中任意两个值的和为给定的值,返回True, 否则返回False
lis = [5,6,9,2,1,3]
num = 13

def dd(lis,num):
	i = 0
	j = 1
	while 1:
		if lis[i] + lis[j] == num:
			print('OK')
			return 
		elif j==len(lis)-1:
			i+=1
			j=0
		elif i==len(lis)-1:
			print('None')
			return 
		else:
			j+=1
	
dd(lis,num)
