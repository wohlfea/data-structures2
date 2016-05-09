# _*_ encoding: utf-8 _*_
import pytest
import io


@pytest.fixture()
def hash_table_20():
    """Fixture that makes a hash table with 20 buckets."""
    from hash_table import HashTable
    ht = HashTable(20)
    return ht


@pytest.fixture()
def big_table():
    """Fixture that makes a hash table with 20 buckets."""
    from hash_table import HashTable
    ht = HashTable(50)
    return ht


@pytest.fixture()
def hash_table_2():
    """Fixture that makes a hash table with 2 buckets."""
    from hash_table import HashTable
    ht = HashTable(2)
    return ht


def test_hash(hash_table_2):
    """Ensure hashing algorithm works as expected."""
    assert hash_table_2._hash('a') == 1


def test_longer_hash(hash_table_20):
    """Check a longer string is hashed as expected."""
    assert hash_table_20._hash('abcdef') == 17


def not_string(hash_table_20):
    """Ensure TypeError raises when key is not string."""
    with pytest.raises:
        hash_table_20.set(10, 'NONO')


def test_set(hash_table_20):
    hash_table_20.set('abcdef', 42)


# def test_set_with_dict(big_table):
#     with io.open('/usr/share/dict/words', 'r', encoding='utf-8') as file:
#         for line in file:
#             big_table.set(str(line), str(line))

@pytest.fixture
def get_words():
    with io.open('/usr/share/dict/words', 'r', encoding='utf-8') as file:
        for line in file:
            yield line

@pytest.fixture
def words_table():
    from hash_table import HashTable
    big_table = HashTable(50)
    for word in get_words():
        big_table.set(str(word), str(word))
    return big_table
