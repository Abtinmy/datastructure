import unittest
from sorts.bubble import (
    bubblesort,
    bubblesort_no_loop,
    bubblesort_optimized,
    bubblesort_recursion
)
import random


class TestBubble(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 5)

    def test_bubblesort(self):
        result = bubblesort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_bubblesort_optimized(self):
        result = bubblesort_optimized(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))
    
    def test_bubblesort_recursion(self):
        result = bubblesort_recursion(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_bubblesort_no_loop(self):
        result = bubblesort_no_loop(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))


    