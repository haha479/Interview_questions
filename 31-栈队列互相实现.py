'''
两个栈实现一个队列
入队：元素进栈A

出队：先判断栈B是否为空，为空则将栈A中的元素 pop 出来并 push 进栈B，再栈B出栈，如不为空则栈B直接出栈

复杂度分析：

这样用两个栈实现一个队列,入队的复杂度为O(1)，出队的复杂度则变为O(n)。
'''
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


'''
两个队列实现一个栈
'''

class Stack(object):
	def __init__(self):
		self.queue1 = []
		self.queue2 = []

	def push(self, item):
		self.queue1.append(item)

	def pop(self):
		if len(self.queue1) == 0:
			return None
		while len(self.queue1) != 1:
			self.queue2.append(self.queue1.pop(0))
		self.queue1, self.queue2 = self.queue2, self.queue1

		return self.queue2.pop()

s = Stack()
s.push('a')
s.push('b')

print(s.pop())
print(s.pop())
