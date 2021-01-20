# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")


"""
列表，1维，最大上升子序列；
数字
case:
[1,9,3,8,2,6,4,5]

[8,9,10,11,1,14,3,0]

x(0) = 1
x(i) = ?
    if x[i]<x[i-1]  = dp[i-1]+1
    if x[i]>=x[i-1]?回溯到的时候，


"""


def maxUp(input):
    if not input or len(input)==0:
        return None
    n = len(input)
    if n==1:
        return 1
    dp = [0]*n
    dp[0] = 1
    for i in xrange(1, n):
        for j in xrange(0, i):
            if input[j]<input[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


input = [1,9,3,8,2,6,4,5]
tmp = maxUp(input)
print(tmp)


def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] = max(m[x], m[y]+1)
    max_value = max(m)
    result = []
    for i in range(n):
        if m[i] == max_value:
            result.append(arr[i])
            max_value -= 1
    return result


arr = [70, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(arr))