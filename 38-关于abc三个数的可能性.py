# 如果a+b+c = 1000, a^2 + b^2 = c^2, 请清楚a,b,c可能的值
import time 

start_time = time.time()
# 第一种程序方式
# for a in range(0,1001):
# 		for b in range(0,1001):
# 			for c in range(0,1001):
# 				if a+b+c == 1000 and a**2 + b**2 == c**2:
# 					print('a, b, c=%d, %d, %d'% (a, b, c))

# 第二种程序方式: 当a和b的值确定后, c的值也可以确定了
for a in range(0,1001):
		for b in range(0,1001):
			c = 1000 - a - b
			if a**2 + b**2 == c**2:
				print('a, b, c=%d, %d, %d'% (a, b, c))
end_time = time.time()


print('times: ', end_time-start_time)
print('finished')