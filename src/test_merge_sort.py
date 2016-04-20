# _*_ encoding: utf-8 _*_
import pytest
from random import randint


RAND_LISTS = [[randint(1, 2000) for x in range(randint(1, 500))] for l in range(1, 2000)]
@pytest.fixture(params=RAND_LISTS)
def rand_list(request):
    return request.param


def test_merge_01():
    from merge_sort import merge
    assert merge([3, 5], [2, 9]) == [2, 3, 5, 9]


def test_merge_02():
    from merge_sort import merge
    assert merge([5], [2]) == [2, 5]


def test_merge_03():
    from merge_sort import merge
    assert merge([5], []) == [5]


def test_merge_04():
    from merge_sort import merge
    assert merge([], []) == []


def test_merge_05():
    from merge_sort import merge
    assert merge([5, 9, 200], [2, 6, 30]) == [2, 5, 6, 9, 30, 200]


def test_merge_sort_01():
    from merge_sort import merge_sort
    assert merge_sort([4, 20, 1, 800, 2, 300, 90, 1]) == [1, 1, 2, 4, 20, 90, 300, 800]


def test_merge_sort_random_01(rand_list):
    from merge_sort import merge_sort
    assert merge_sort(rand_list) == sorted(rand_list)
