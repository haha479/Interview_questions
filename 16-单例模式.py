class Singleton(object):
	__isinstance = None
	def __new__(cls):
		if cls.__isinstance is None:
			cls.__isinstance = object.__new__(cls)

		return cls.__isinstance


a = Only()
b = Only()

print(id(a))
print(id(b))
