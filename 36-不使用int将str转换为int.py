from functools import reduce
st = "13579"
def str_int(st):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	def fn(x,y):
		return x*10+y

	def char2num(s):
		return digits[s]

	return reduce(fn, (map(char2num, st)))

# print(str_int(st))
str_int(st)