# -*- conding:utf-8 -*-
import queue

q = queue.Queue(5)
for i in range(5):
	print('将%s加入到队列'%i)
	q.put(i)

print('队列中长度:',q.qsize())
print('取出队列中一个元素:',q.get())

