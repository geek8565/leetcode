# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")

"""
查找一个数组内最大的k个树
"""

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(arr)
        for i in range(size, -1, -1):
            self.heapify(arr, size, i)
        for i in range(size - 1, size-k-1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr[size-k:]

    def _getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(arr)
        arr = self.quickSort(arr, 0, size - 1, k)
        return arr[:k]

    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def quickSort(self, nums, l, r, k):
        if l < r:
            pi = self.partition(nums, l, r)
            num = pi - l + 1
            if k < num:
                self.quickSort(nums, l, pi - 1, k)
            elif k > num:
                self.quickSort(nums, pi + 1, r, k - num)
        return nums

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] < arr[largest]:
            largest = l
        if r < n and arr[r] < arr[largest]:
            largest = r
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)

arr = [70, 22, 9, 33, 21, 50, 41, 60, 80]

head = Solution()
print(head.getLeastNumbers(arr, 3))