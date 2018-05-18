
def singleton(cls):
	_instance = {}
	def singleton_inner():
		if cls not in _instance :
			_instance[cls] = cls()
		return _instance[cls]
	return singleton_inner

@singleton
class A(object):
	def __init__(self):
		self.name = None

a1 = A()
a2 = A()

print(id(a1))
print(id(a2))
