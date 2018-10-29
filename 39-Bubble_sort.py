def Bubble(alist):
    n = len(alist)
    for j in range(0,n-1):
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    Bubble(alist)
    print(alist)


'''
冒泡排序的最优时间复杂度: O(n)
最坏时间复杂度: O(n2)
冒泡排序的原理:1.从第一个数开始, 与后面相邻的数做对比, 大的数放到后面,
如果容器的长度是n, 需要对比的次数就是n-1, 对比n-1次之后, 最后面的数
应该是容器中最大的.
2.如上的步骤需要执行n次(容器中有n个元素), 但每执行一次, 容器中就会确认一个数的排序在最后,步骤1就可以少执行一次(n-1-j的由来)
内循环表示步骤2, 外循环表示步骤1
'''



