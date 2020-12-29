# -*- coding: utf-8 -*-
from __future__ import print_function

from . import bubbleSort
from . import selectionSort
from . import insertionSort
from . import shellSort
from . import mergeSort
from . import quickSort
from . import heapSort
from . import countingSort
from . import bucketSort
from . import radixSort

# global functions  全局函数：代码常调用函数
# 1.冒泡排序    稳定      n^2
bubble_sort = bucketSort.bucketSort

# 2.选择排序    不稳定    n^2
selection_sort = selectionSort.selectionSort

# 3.插入排序    稳定      n^2
insertion_sort = insertionSort.insertionSort

# 4.希尔排序    不稳定     n^1.3
shell_sort = shellSort.shellSort

# 5.归并排序    稳定      nlog2n
merge_sort = mergeSort.mergeSort

# 6.快速排序    不稳定     nlog2n
quick_sort = quickSort.quickSort

# 7.堆排序     不稳定     nlog2n
heap_sort = heapSort.heapSort

# 8.计数排序    稳定      n+k
counting_sort = countingSort.countingSort

# 9.桶排序     稳定      n+k
bucket_sort = bucketSort.bucketSort

# 10.基数排序   稳定      n+l
radix_sort = radixSort.radixSort