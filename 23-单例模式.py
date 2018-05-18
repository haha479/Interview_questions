class Singleton(object):
	def __new__(cls):
		if not hasattr(cls,'_isinstance'):
			cls._isinstance = object.__new__(cls)

		return cls._isinstance

a = Singleton()
b = Singleton()

print(id(a))

print(id(b))

