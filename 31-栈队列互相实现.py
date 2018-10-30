# 两个栈实现一个队列
class Queue(object):
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, item):
		self.stack1.append(item)

	def pop(self):
		if self.stack2 == []:
			if self.stack1 == []:
				return None
			else:
				for i in range(len(self.stack1)):
					self.stack2.append(self.stack1.pop())
		return self.stack2.pop()


q = Queue()
q.push(1)
q.push(2)

print(q.pop())
print(q.pop())
