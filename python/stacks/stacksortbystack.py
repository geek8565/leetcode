# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import copy

reload(sys)
sys.setdefaultencoding("utf-8")

"""
只能用一个二外的栈来对已知的栈进行排序，可以使用有限的中间变量

用一个栈实现另外一个栈的顶到底降序排序

要求：不能使用额外的数据结构，但可以使用新的变量。

Tower of Hanoi
汉诺塔

"""

def sort(stack):
    help = []
    while stack:
        cur = stack.pop()
        while len(help)>0:
            tmp = help.pop()
            if tmp<cur:
                stack.append(tmp)
                continue
            else:
                help.append(tmp)
                break
        help.append(cur)
    return help

arr = [70, 22, 9, 33, 21, 50, 41, 60, 80]
print(sort(arr))