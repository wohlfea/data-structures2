# _*_ encoding: utf-8 _*_
import pytest


@pytest.fixture()
def full_trie():
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    new_trie.insert('trie')
    new_trie.insert('trip')
    new_trie.insert('in')
    new_trie.insert('i')
    new_trie.insert('worldly')
    return new_trie


def test_trie():
    """Test that we can insert into the Trie."""
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    assert new_trie.root == {'w': {'o': {'r': {'d': {'s': {'$': '$'}}}}}}


def test_2_trie():
    """Test that we can insert two words into the Trie."""
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    new_trie.insert('trie')
    assert new_trie.root == {'w': {'o': {'r': {'d': {'s': {'$': '$'}}}}},
                             't': {'r': {'i': {'e': {'$': '$'}}}}}


def test_overlapping_words():
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    new_trie.insert('trie')
    new_trie.insert('trip')
    assert new_trie.root == {'w': {'o': {'r': {'d': {'s': {'$': '$'}}}}},
                             't': {'r': {'i': {'e': {'$': '$'}, 'p': {'$': '$'}}}}}


def test_overlapping_words_no_duplication():
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    new_trie.insert('trie')
    new_trie.insert('trip')
    new_trie.insert('in')
    new_trie.insert('i')
    assert new_trie.root == {'w': {'o': {'r': {'d': {'s': {'$': '$'}}}}},
                             't': {'r': {'i': {'e': {'$': '$'}, 'p': {'$': '$'}}}},
                             'i': {'n': {'$': '$'}, '$': '$'}}


def test_overlapping_words_no_duplication_empty_string():
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    new_trie.insert('trie')
    new_trie.insert('trip')
    new_trie.insert('in')
    new_trie.insert('i')
    new_trie.insert('')
    assert new_trie.root == {'w': {'o': {'r': {'d': {'s': {'$': '$'}}}}},
                             't': {'r': {'i': {'e': {'$': '$'}, 'p': {'$': '$'}}}},
                             'i': {'n': {'$': '$'}, '$': '$'}}


def test_overlapping_words_no_duplication_number():
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    new_trie.insert('trie')
    new_trie.insert('trip')
    new_trie.insert('in')
    new_trie.insert('i')
    new_trie.insert(3)
    assert new_trie.root == {'w': {'o': {'r': {'d': {'s': {'$': '$'}}}}},
                             't': {'r': {'i': {'e': {'$': '$'}, 'p': {'$': '$'}}}},
                             'i': {'n': {'$': '$'}, '$': '$'}}


def test_overlapping_words_no_duplication_many_letters():
    from trie import Trie
    new_trie = Trie()
    new_trie.insert('words')
    new_trie.insert('trie')
    new_trie.insert('trip')
    new_trie.insert('in')
    new_trie.insert('i')
    new_trie.insert('worldly')
    assert new_trie.root == {'w': {'o': {'r': {'d': {'s': {'$': '$'}},
                             'l': {'d': {'l': {'y': {'$': '$'}}}}}}},
                             't': {'r': {'i': {'e': {'$': '$'}, 'p': {'$': '$'}}}},
                             'i': {'n': {'$': '$'}, '$': '$'}}


def test_full_trie_contains(full_trie):
    assert full_trie.contains('words') is True


def test_full_trie_contains_number(full_trie):
    assert full_trie.contains(2) is False


def test_full_trie_contains_deeper_word(full_trie):
    assert full_trie.contains('worldly') is True


def test_full_trie_contains_half_word(full_trie):
    assert full_trie.contains('wor') is False


def test_full_trie_contains_too_long(full_trie):
    assert full_trie.contains('worldlystuffs') is False


def test_full_trie_contains_other_words(full_trie):
    assert full_trie.contains('i') is True


def test_full_trie_contains_other_words_2(full_trie):
    assert full_trie.contains('in') is True


def test_full_trie_contains_cash_money(full_trie):
    assert full_trie.contains('$') is False


def test_full_trie_contains_conjunctions(full_trie):
    full_trie.insert('don\'t')
    assert full_trie.contains('don\'t') is True


def test_small_traversal():
    from trie import Trie
    my_trie = Trie()
    my_trie.insert('word')
    my_trie.insert('worldly')
    my_trie.insert('otherword')
    assert sorted([x for x in my_trie.traversal()]) == ['otherword', 'word', 'worldly']


def test_large_traversal(full_trie):
    assert sorted([x for x in full_trie.traversal()]) == ['i', 'in', 'trie', 'trip', 'words', 'worldly']


def test_empty_trie():
    from trie import Trie
    empty = Trie()
    assert [x for x in empty.traversal()] == []


def test_single_trie_traversal():
    from trie import Trie
    single = Trie()
    single.insert('one')
    assert [x for x in single.traversal()] == ['one']


def test_single_apostrophe():
    from trie import Trie
    single = Trie()
    single.insert('don\'t')
    assert [x for x in single.traversal()] == ['don\'t']


def test_autocomplete(full_trie):
    autoc = full_trie.autocomplete('in')
    for key in autoc.keys():
        autoc[key] = sorted(autoc[key])
    assert autoc == {'i': ['i', 'in'], 'in': ['in']}


def test_autocomplete2(full_trie):
    autoc = full_trie.autocomplete('into')
    for key in autoc.keys():
        autoc[key] = sorted(autoc[key])
    assert autoc == {'i': ['i', 'in'], 'in': ['in'], 'int': [], 'into': []}



