from main import *

def test_calculate_product():
    assert calculate_product([3, 5, -2, 7]) == -210
    assert calculate_product([3, 0, -2, 7]) == 0

def test_calculate_average():
    assert calculate_average([3, 6, 9, 12, 15, 21]) == 11.0
    assert calculate_average([7, -3, 4, 1, 0]) == 1.8

def test_count_evens():
    assert count_evens([4, 5, -7, 1, 0, 6, -8]) == 4
    assert count_evens([4, 2, -70, 18, 0, 6, -8]) == 7
    assert count_evens([41, 5, -7, 1, 9, -5, -13]) == 0

def test_count_words_with_given_length():
    assert count_words_with_given_length(['hi', 'want', 'to', 'as', 'and', 'help'], 2) == 3
    assert count_words_with_given_length(['hi', 'want', 'to', 'as', 'and', 'help'], 3) == 1
    assert count_words_with_given_length(['hi', 'want', 'to', 'as', 'and', 'help'], 4) == 2

def test_count_vowels():
    assert count_vowels('hibernate') == 4
    assert count_vowels('school') == 2
    assert count_vowels('luxuriate') == 5

def test_count_divisible_by_num():
    assert count_divisible_by_num([-9, 5, 21, 4, 6, 7, 22, -2, 15], 3) == 4
    assert count_divisible_by_num([-9, 5, 21, 4, 6, 7, 22, -2, 15], 5) == 2
    assert count_divisible_by_num([-9, 5, 21, 4, 6, 7, 22, -2, 15], 11) == 1