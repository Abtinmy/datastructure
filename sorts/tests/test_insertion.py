import unittest
import sorts.insertionsort
import random


class TestInsertion(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)

    def test_insertionsort(self):
        result = sorts.insertionsort.insertionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_recursive_insertionsort(self):
        result = sorts.insertionsort.recursive_insertionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))
    
    def test_insertionsort_even_odd(self):
        odd_even_list = [5, 8, 4, 3, 9, 2, 7, 6, 1]
        expected_odd_even_list = [9, 2, 7, 3, 5, 6, 4, 8, 1]
        result = sorts.insertionsort.insertionsort_even_odd(odd_even_list)
        self.assertListEqual(result, expected_odd_even_list)


    