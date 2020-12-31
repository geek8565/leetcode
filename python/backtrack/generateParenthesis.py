# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

# 回溯算法

def generateParenthesis(n):
    ans = []
    def backtrack(S, left, right):
        if len(S) == 2 * n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S, left +1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S, left, right +1)
            S.pop()

    backtrack([], 0, 0)
    return ans


res = generateParenthesis(3)
print(res)