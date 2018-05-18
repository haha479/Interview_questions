import threading
from queue import Queue
import time


class Producer(threading.Thread):
	def run(self):
		global queue
		count = 0
		while True :
			if queue.qsize()< 1000:
				# 向队列中添加500个产品
				for i in range(500):
					count += 1
					msg = '生产产品' + str(count)
					queue.put(msg)
					print(msg)
			time.sleep(0.5)
		

class Consumer(threading.Thread):
	def run(self):
		global queue
		while True :
			if queue.qsize() > 100:
				for i in range(3):
					msg = self.name + '消费了' + queue.get()
					print(msg)
			time.sleep(1)


# 创建队列
queue = Queue()

# 初始队列中添加500个产品
for i in range(500):
	msgs = '初始产品' + str(i)
	queue.put(msgs)

# 创建2个线程用于生产
for i in range(2):
	pro = Producer()
	pro.start()

# 创建5个线程用于消费
for i in range(5):
	con = Consumer()
	con.start()



