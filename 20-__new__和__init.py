class Data(object):
	def __init__(self, name):
		self.name = name
		print('self.name==',self.name)
		print('init执行')

	def __new__(cls, *args, **kwargs):
		print('new执行')
		obj = object.__new__(cls)
		print('new中返回的对象=',obj)
		# 这里返回的就是实例对象,也就是init接收的self
		return obj


data = Data('haha')


print ('实例对象data=',data)