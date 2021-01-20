# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")


"""
计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

所以是一个用空间换时间的排序算法
"""

def countingSort(arr, maxK):
    size = len(arr)
    res = [0 for _ in range(size)]
    count = [0 for _ in range(maxK+1)]
    for i in arr:
        count[i] +=1
    print(count)

    for i in range(1, len(count)):
        count[i] +=count[i-1]
    print(count)
    for i in arr:
        res[count[i]-1] = i
        count[i]-= 1
    return res

array = [1,3,8,4,6,9,2,5]
result = countingSort(copy.copy(array), 9)
print("输入：")
print(array)
print("输出：")
print(result)
