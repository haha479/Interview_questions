class A(object):
	def go(self):
		print('go a')
	def stop(self):
		print('stop a')
	def pause(self):
		raise Exception('not im')


class B(A):
	def go(self):
		super(B, self).go()
		print('go b')

class C(A):
	def go(self):
		super(C, self).go()
		print('go c')
	def stop(self):
		super(C, self).stop()
		print('stop c')

class D(B, C):
	def go(self):
		super(D, self).go()
		print('go d')

	def stop(self):
		super(D, self).stop()
		print('stop d')

	def pause(self):
		print('wait d')

class E(B, C):
	pass

a = A()
b = B()
c = C()
d = D()
e = E()

a.go()
print('----')
b.go()
print('----')
c.go()
print('----')
d.go()
print('----')
e.go()
print('----')


a.stop()
print('----')
b.stop()
print('----')
c.stop()
print('----')
d.stop()
print('----')
e.stop()
print('----')