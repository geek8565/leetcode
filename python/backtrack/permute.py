# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

# 回溯算法

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    n = len(nums)
    res = []

    def backtrack(index):
        if index == n:
            res.append(nums[:])
        for i in range(index, n):
            nums[index], nums[i] = nums[i], nums[index]
            backtrack(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    backtrack(0)
    return res


nums = [1,2,3]
res = permute(nums)
print(res)