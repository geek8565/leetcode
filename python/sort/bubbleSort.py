# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")


"""
按数据把全局最大发射到最顶端，边找边交换
O(n²)
稳定
"""

def bubbleSort(array):
    # 数组大小
    size = len(array)
    # 遍历所有数组
    for i in range(size):
        # 从开始位置按顺序，把最大的冒泡到顶端
        for j in range(0,size-1-i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array = [1,3,8,4,6,9,2,10]
result = bubbleSort(copy.copy(array))
print("输入：")
print(array)
print("输出：")
print(result)