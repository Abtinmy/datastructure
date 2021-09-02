import unittest
from sorts.selection import (
    selectionsort,
    stable_selectionsort,
    optimized_selectionsort, 
    recursive_selectionsort
)
import random


class TestSelection(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)

    def test_selectionsort(self):
        result = selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_recursive_selectionsort(self):
        result = recursive_selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))
    
    def test_optimized_selectionsort(self):
        result = optimized_selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_stable_selectionsort(self):
        result = stable_selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))


    