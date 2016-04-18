# _*_ encoding: utf-8 _*_


def test_sort_unordered():
    """Unordered list becomes ordered."""
    from insertion_sort import insertion_sort
    nums = [33, 22, 45, 81, 73]
    assert insertion_sort(nums) == [22, 33, 45, 73, 81]


def test_sort_ordered():
    """Sorted list stays sorted."""
    from insertion_sort import insertion_sort
    nums = [x for x in range(50, 100)]
    assert insertion_sort(nums) == [x for x in range(50, 100)]


def test_single_item():
    """Verify single item list works."""
    from insertion_sort import insertion_sort
    nums = [2]
    assert insertion_sort(nums) == [2]


def test_empty():
    """Verify empty list is returned for empty list."""
    from insertion_sort import insertion_sort
    nums = []
    assert insertion_sort(nums) == []


def test_tuple():
    """Verify that the same algorithm works on tuples."""
    from insertion_sort import insertion_sort_tuples
    nums = [('a', 5), ('b', 30), ('D', 1)]
    assert insertion_sort_tuples(nums) == [('D', 1), ('a', 5), ('b', 30)]


def test_stable():
    """Verify that same values remain in the same relative position throughout the sort."""
    from insertion_sort import insertion_sort_tuples
    nums = [('a', 5), ('A', 30), ('D', 1), ('b', 30)]
    assert insertion_sort_tuples(nums) == [('D', 1), ('a', 5), ('A', 30), ('b', 30)]
