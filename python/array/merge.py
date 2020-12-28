# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

class merge():
    """
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

    说明：

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    """

    def process(self, nums1, m, nums2, n):
        # 三个指针定义，倒序进行归并
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]<nums2[p2]:
                nums1[p] = nums2[p2]
                p2-=1
            else:
                nums1[p] = nums1[p1]
                p1-=1
            p-=1
        nums1[:p2+1] = nums2[:p2+1]
        return nums1



if __name__ == "__main__":
    engine = merge()
    num1=[1,2,3,0,0,0]
    num2=[2, 5, 6]
    m=3
    n=3
    result = engine.process(num1, m, num2, n)
    print("输出：")
    print(result)