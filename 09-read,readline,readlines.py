
f = open('09-test.txt','r')
# 读取所有内容
# text = f.read()
# print(text)

# for i in range(1,20):
	# 读取一行内容
# 	text = f.readline()
# 	print(text)

# 读取所有内容,并且分行
text = f.readlines()
for i in text :
	print(i)

f.close()