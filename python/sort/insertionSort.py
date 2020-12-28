# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")

"""
每次找局部最小的，比较并挪动；
O(n²)
稳定
"""



def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        preIndex = i-1
        current = array[i]
        while preIndex>=0 and array[preIndex]>current:
            array[preIndex+1] = array[preIndex]
            preIndex -= 1
        array[preIndex+1] = current
    return array



array = [1,3,8,4,6,9,2,10]
result = insertionSort(copy.copy(array))
print("输入：")
print(array)
print("输出：")
print(result)