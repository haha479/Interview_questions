def judgment(num):
	return str(num) == str(num)[::-1]

print(list(filter(judgment, range(1000))))
