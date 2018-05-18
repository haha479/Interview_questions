class Person(object):
	def __init__(self):
		self.gender = None
		self.name = None
	def getName(self):
		return self.name

	def getGender(self):
		return self.gender

class Factory(object):
	def getPerson(self, name, gender):
		# 如果创建的"人"对象是男性,就会创建Male的实例对象
		if gender == 'M':
			return Male(name)
		# 如果创建的"人"对象是女性,就会创建female的实例对象
		elif gender == 'F':
			return Female(name)


class Male(Person):
	def __init__(self, name):
		print('hello Mr ', name)


class Female(Person):
	def __init__(self, name):
		print('hello miss ',name)


if __name__ == '__main__':
	factory = Factory()
	person1 = factory.getPerson('haha','M')
	person2 = factory.getPerson('hehe','F')