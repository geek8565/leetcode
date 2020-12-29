# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")


"""
桶排序是计数排序的升级版。
它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
桶排序 (Bucket sort)的工作的原理：
    假设输入数据服从均匀分布，
    将数据分到有限数量的桶里，
    每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
    
核心的问题在于如何分桶

"""

def insertSort(a):
    n=len(a)
    if n<=1:
        return
    for i in range(1,n):
        key=a[i]
        j=i-1
        while key<a[j] and j>=0:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key

def bucketSort(a):
    n=len(a)
    s=[[] for _ in xrange(n)]
    for i in a:
        s[int(i*n)].append(i)
    for i in s:
        insertSort(i)
    return [i for j in s for i in j]


from random import random

# 区间[0, 1)均匀分布的桶排序
# 数据均匀分布，桶的分布会更均匀。所以这个也通排序的应用场景问题
a=[random() for i in xrange(100)]
result = bucketSort(copy.copy(a))


print(a)
print(result)