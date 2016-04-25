# _*_ encoding: utf-8 _*_
from random import randint
import pytest


RAND_LISTS = [[randint(1, 2000) for x in range(randint(1, 500))] for l in range(1, 2000)]


@pytest.fixture(params=RAND_LISTS)
def rand_list(request):
    return request.param


def test_quicksort_random_01(rand_list):
    from quicksort import quicksort
    assert quicksort(rand_list) == sorted(rand_list)


def test_quicksort_empty_list():
    from quicksort import quicksort
    assert quicksort([]) == []


def test_quicksort_1item_list():
    from quicksort import quicksort
    assert quicksort([1]) == [1]

