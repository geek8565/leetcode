# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")

"""
基数排序是按照低位先排序，然后收集；
再按照高位排序，然后再收集；
依次类推，直到最高位。
有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。
最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。

其实，基数排序也是桶排序的一种新形势；只不过是一种特殊的分通规则
"""



def radixSort(lis, d):
    for i in xrange(d):#d轮排序
        s = [[] for _ in xrange(10)]#因为每一位数字都是0~9，故建立10个桶
        for j in lis:
            s[j/(10**i)%10].append(j)
        lis = [a for b in s for a in b]
    return lis


array = [111,304,81,45,69,98,214,159]
result = radixSort(copy.copy(array), 3)
print("输入：")
print(array)
print("输出：")
print(result)
