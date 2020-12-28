# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")
# nlogn 稳定

def merge(left, right):
    merge_result = []
    h = j = 0
    while j < len(left) and h < len(right):
        if left[j] < right[h]:
            merge_result.append(left[j])
            j += 1
        else:
            merge_result.append(right[h])
            h += 1

    if j == len(left):
        for i in right[h:]:
            merge_result.append(i)
    else:
        for i in left[j:]:
            merge_result.append(i)
    return merge_result


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


array = [1,3,8,4,6,9,2,10]
result = mergeSort(copy.copy(array))
print("输入：")
print(array)
print("输出：")
print(result)