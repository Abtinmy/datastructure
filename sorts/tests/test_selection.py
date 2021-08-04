import unittest
import sorts.selectionsort
import random


class TestSelection(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)

    def test_selectionsort(self):
        result = sorts.selectionsort.selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_recursive_selectionsort(self):
        result = sorts.selectionsort.recursive_selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))
    
    def test_optimized_selectionsort(self):
        result = sorts.selectionsort.optimized_selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_stable_selectionsort(self):
        result = sorts.selectionsort.stable_selectionsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))


    