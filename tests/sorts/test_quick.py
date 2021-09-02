import unittest
from sorts.quick import (
    quicksort,
    lomuto_quicksort,
    random_quicksort,
    stable_quicksort,
    optimized_quicksort,
    dual_pivot_quicksort
)
import random


class TestQuick(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)

    def test_quicksort(self):
        result = quicksort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_lomuto_quicksort(self):
        result = lomuto_quicksort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_random_quicksort(self):
        result = random_quicksort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))
    
    def test_stable_quicksort(self):
        result = stable_quicksort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_optimized_quicksort(self):
        result = optimized_quicksort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_dual_pivot_quicksort(self):
        result = dual_pivot_quicksort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))
 