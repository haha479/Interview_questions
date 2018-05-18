class Only(object):
	__isinstance = None
	def __init__(self,name):
		self.name = name
	def __new__(cls,name):
		if cls.__isinstance is None:
			cls.__isinstance = object.__new__(cls)

		return cls.__isinstance


a = Only('haha')

b = Only('hehe')

print(id(a))
print(id(b))
