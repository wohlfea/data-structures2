# _*_ encoding: utf-8 _*_
from __future__ import division
import timeit
import random


def radix_sort(nums):
    """Radix sort implementation."""
    if not nums:
        return nums
    tens = 10
    for iteration in range(len(str(max(nums)))):
        buckets = [[] for x in range(10)]
        for num in nums:
            buckets[(num % tens) // (tens // 10)].append(num)
        tens *= 10
        nums = [num for li in buckets for num in li]
    return nums


if __name__ == '__main__':
    print("""
The radix sort algorithm sorts each item by its ones, tens, hundreds.. etc value into buckets, reassembles and sorts again.
The larger the number, the slower the sort.

Here are the best and worst case scenarios:

Input (Worst Case Scenario):

lst_one = [random.randint(100000, 900000) for x in range(0, 2000)]
    """)
    lst_one = [random.randint(100000, 900000) for x in range(0, 2000)]
    time1 = timeit.timeit('radix_sort(lst_one)', setup="from __main__ import radix_sort, lst_one",number=500)
    print("""
Number of runs = 500
Average Time = {}


Input (Best Case Scenario):

lst_two = [random.randint(0, 9) for x in range(0, 2000)]
    """.format(time1))
    lst_two = [random.randint(0, 9) for x in range(0, 2000)]
    time2 = timeit.timeit('radix_sort(lst_two)', setup="from __main__ import radix_sort, lst_two",number=500)
    print("""
Number of runs = 500
Average Time = {}
    """.format(time2))
