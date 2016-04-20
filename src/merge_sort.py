# _*_ encoding: utf-8 _*_
"""Implementation of a merge sort algorithm"""


def merge_sort(vals):
    if len(vals) <= 1:
        return vals
    left = [num for ind, num in enumerate(vals) if ind % 2]
    right = [num for ind, num in enumerate(vals) if not ind % 2]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result
