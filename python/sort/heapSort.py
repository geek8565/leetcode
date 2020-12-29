# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")


"""
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
堆排序可以说是一种利用堆的概念来排序的选择排序。
"""


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)
    print("debug")
    print(arr)


def heapSort(arr):
    size = len(arr)
    # 构建最大堆
    for i in range(size, -1, -1):
        heapify(arr, size, i)

    # 一个一个的交换
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


array = [1,3,8,4,6,9,2,5]
result = heapSort(copy.copy(array))
print("输入：")
print(array)
print("输出：")
print(result)
