import os
import shutil

print(os.listdir())

# 删除指定文件
# os.remove('18-test.txt')


# 将test1中的内容复制到test2中
shutil.copyfile('18-test1.txt','18-test2.txt')


