# _*_ encoding: utf-8 _*_
"""Implementation of a merge sort algorithm"""
import timeit

def merge_sort(vals):
    if len(vals) <= 1:
        return vals
    left = merge_sort(vals[::2])
    right = merge_sort(vals[1::2])
    return merge(left, right)


def merge(left, right):
    result = []
    l_ind = 0
    r_ind = 0
    while l_ind <= len(left) - 1 and r_ind <= len(right) - 1:
        if left[l_ind] <= right[r_ind]:
            result.append(left[l_ind])
            l_ind += 1
        else:
            result.append(right[r_ind])
            r_ind += 1
    result += left[l_ind:]
    result += right[r_ind:]
    return result


if __name__ == '__main__':
    print("""
The merge sort algorithm recursively splits the list into smaller lists, sorts and then merges the two lists.

Here are the best and worst case scenarios:

Input (Worst Case Scenario):

lst_one = [x for x in range(0, 2000)]
lst_one.reverse()
    """)
    lst_one = [x for x in range(0, 2000)]
    lst_one.reverse()
    time1 = timeit.timeit('merge_sort(lst_one)', setup="from __main__ import merge_sort, lst_one",number=500)
    print("""
Number of runs = 500
Average Time = {}


Input (Best Case Scenario):

lst_two = [x for x in range(0, 2000)]
    """.format(time1))
    lst_two = [x for x in range(0, 2000)]
    time2 = timeit.timeit('merge_sort(lst_two)', setup="from __main__ import merge_sort, lst_two",number=500)
    print("""
Number of runs = 500
Average Time = {}
    """.format(time2))
