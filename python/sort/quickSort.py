# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")


"""
分治思想，随机经一个分界元素，把比这个小的放在左侧，把比这个大的放在右侧
然后递归调用就可以了。
nlog2n
不稳定
"""

# 分区
def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j]<=pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i+1

# 递归调用
def quickSort(arr, low, high):
    if low<high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr


array = [1,3,8,4,6,9,2,5]
result = quickSort(copy.copy(array), 0, len(array)-1)
print("输入：")
print(array)
print("输出：")
print(result)
