import unittest
import sorts.bubblesort
import random


class TestBubble(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 5)

    def test_bubblesort(self):
        result = sorts.bubblesort.bubblesort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_bubblesort_optimized(self):
        result = sorts.bubblesort.bubblesort_optimized(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))
    
    def test_bubblesort_recursion(self):
        result = sorts.bubblesort.bubblesort_recursion(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_bubblesort_no_loop(self):
        result = sorts.bubblesort.bubblesort_no_loop(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))


    