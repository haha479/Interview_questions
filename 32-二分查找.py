def binarysearch(alist, num):
    length = len(alist)
    low = 0
    # high: 索引最大值
    high = length - 1
    while low <= high:
        mid = int(low + ((high - low) / 2)) ##使用(low+high)/2会有整数溢出的问题
        if alist[mid] < num:
            low = mid + 1
        elif alist[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1
 
 
if __name__ == '__main__':
    lis = [5, 3, 4, 8, 22, 65, 73, 90]

    print(binarysearch(lis, 65))