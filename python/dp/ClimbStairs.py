# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

class climbStairs():
    """
    *假设你正在爬楼梯。需要n阶你才能到达楼顶。
    *每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？

    * 这是一个动态规划问题：
    * 	1.找到初始条件 x 0 =0 y 0 =0, x 1 =1 y 1 =1, x 2 =2 y 2 =2, x 3 =3 y 3 =y 1 +y2;
    * 	2.找到表达式 f(x ) =f(x−1)+f(x−2) */
    """

    def process(self, n):
        if n<=0:
            return 0
        first, second, result = 0, 0, 1
        for _ in range(1, n+1):
            first = second
            second = result
            result = first+second
        return result



if __name__ == "__main__":
    engine = climbStairs()
    input = 4
    result = engine.process(input)
    print("输入：")
    print(input)
    print("输出：")
    print(result)