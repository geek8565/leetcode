# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")



"""
每次找全局最小的，找而不交换，最后交换一次；
O(n²)
不稳定
"""


def selectionSort(array):
    size = len(array)
    for i in range(size):
        minIndex = i
        for j in range(i+1, size):
            if array[j]<array[i]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array

array = [1,3,8,4,6,9,2,10]
result = selectionSort(copy.copy(array))
print("输入：")
print(array)
print("输出：")
print(result)