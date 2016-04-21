# _*_ encoding: utf-8 _*_
import random
import timeit


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    low = []
    high = []
    pivot = nums[len(nums) // 2]
    for num in nums:
        if num < pivot:
            low.append(num)
        if num > pivot:
            high.append(num)
    low = quicksort(low)
    high = quicksort(high)
    return low + [pivot] * nums.count(pivot) + high



if __name__ == '__main__':
    print("""
The quick sort algorithm takes a selected pivot value and sorts values
into lists based on their relationship to the pivot value. The new list
with sorted values is returned.

Here are the best and worst case scenarios:

Input (Worst Case Scenario):

lst_one = [x for x in range(0, 2000)]
lst_one.reverse()
    """)
    lst_one = [x for x in range(0, 2000)]
    lst_one.reverse()
    time1 = timeit.timeit('quicksort(lst_one)', setup="from __main__ import quicksort, lst_one",number=500)
    print("""
Number of runs = 500
Average Time = {}


Input (Best Case Scenario):

lst_two = [x for x in range(0, 2000)]
    """.format(time1))
    lst_two = [x for x in range(0, 2000)]
    time2 = timeit.timeit('quicksort(lst_two)', setup="from __main__ import quicksort, lst_two",number=500)
    print("""
Number of runs = 500
Average Time = {}
    """.format(time2))
