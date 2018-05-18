# -*- coding:utf-8 -*-
import pickle

# 写入文件
data = {
	'name_lis':['haha','hehe'],
	'age':18,
	'kaka':('hello world')
}

file = open('19-test.pk1','wb')
pickle.dump(data,file)
file.close()

# 打开写好的文件,用来输出内容
pk1_file = open('19-test.pk1','rb')
content = pickle.load(pk1_file)
print content
pk1_file.close()
