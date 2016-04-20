# _*_ encoding: utf-8 _*_
import timeit


def insertion_sort(nums):
    """Insertion Sort."""
    for index in range(1, len(nums)):
        val = nums[index]
        left_index = index - 1
        while left_index >= 0 and nums[left_index] > val:
            nums[left_index + 1] = nums[left_index]
            left_index -= 1
        nums[left_index + 1] = val
    return nums


def insertion_sort_tuples(nums):
    """Insertion Sort."""
    for index in range(1, len(nums)):
        val = nums[index]
        left_index = index - 1
        while left_index >= 0 and nums[left_index][1] > val[1]:
            nums[left_index + 1] = nums[left_index]
            left_index -= 1
        nums[left_index + 1] = val
    return nums


if __name__ == '__main__':
    print("""
The insertion sort algorithm sorts each item sequentially and compares its value
to its neighbor, working its way to the end of the list and moving smaller items to the left.

Here are the best and worst case scenarios:

Input (Worst Case Scenario):

lst_one = [x for x in range(0, 2000)]
lst_one.reverse()
    """)
    lst_one = [x for x in range(0, 2000)]
    lst_one.reverse()
    time1 = timeit.timeit('insertion_sort(lst_one)', setup="from __main__ import insertion_sort, lst_one",number=500)
    print("""
Number of runs = 500
Average Time = {}


Input (Best Case Scenario):

lst_two = [x for x in range(0, 2000)]
    """.format(time1))
    lst_two = [x for x in range(0, 2000)]
    time2 = timeit.timeit('insertion_sort(lst_two)', setup="from __main__ import insertion_sort, lst_two",number=500)
    print("""
Number of runs = 500
Average Time = {}
    """.format(time2))
