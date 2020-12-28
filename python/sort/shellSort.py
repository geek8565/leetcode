# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")

def shellSort(arr):
    size = len(arr)
    gap = size//2
    while gap>0:
        for i in range(gap, size):
            tmp = arr[i]
            j = i
            while j>=gap and arr[j-gap]>tmp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = tmp
        gap = gap//2
    return arr


array = [1,3,8,4,6,9,2,10]
result = shellSort(copy.copy(array))
print("输入：")
print(array)
print("输出：")
print(result)