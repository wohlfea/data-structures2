# _*_ encoding: utf-8 _*_
import pytest
from random import randint


RAND_LISTS = [[randint(1, 2000) for x in range(randint(1, 500))] for l in range(1, 2000)]


@pytest.fixture(params=RAND_LISTS)
def rand_list(request):
    return request.param


def test_radix_sort_many(rand_list):
    from radix_sort import radix_sort
    assert radix_sort(rand_list) == sorted(rand_list)


def test_radix_empty():
    from radix_sort import radix_sort
    assert radix_sort([]) == []


def test_radix_single():
    from radix_sort import radix_sort
    assert radix_sort([4]) == [4]


def test_radix_two():
    from radix_sort import radix_sort
    assert radix_sort([2342, 892, 200]) == [200, 892, 2342]


def test_radix_zeros():
    from radix_sort import radix_sort
    assert radix_sort([300, 400, 700, 200, 100, 50]) == sorted([300, 400, 700, 200, 100, 50])


def test_radix_big_small():
    from radix_sort import radix_sort
    assert radix_sort([2, 146592387456923847652943]) == sorted([2, 146592387456923847652943])
