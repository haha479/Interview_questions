# -*- coding:utf-8 -*-
import threading
import threadpool
import time


def sayhello(str):
	print('hello',str)
	time.sleep(2)

name_list = ['aa','bb','cc','dd']

# 定义线程池,表示最多可以创建10个线程
pool = threadpool.ThreadPool(10)

# 调用makeRequests创建了要开启多线程的函数，以及函数相关参数和回掉函数
requests = threadpool.makeRequests(sayhello,name_list)

# 将所有要运行多线程的请求扔进线程池,等同于下面第二行开始
[pool.putRequest(req) for req in requests]
# for req in requests:
# 	pool.putRequest(req)

# 等待所有线程完成工作后退出
pool.wait()
















