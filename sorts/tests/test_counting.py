import unittest
from sorts.counting import (
    countingsort,
    countingsort_neg_num
)
import random


class TestCounting(unittest.TestCase):

    def setUp(self):
        self.sample_list = []
        for i in range(10):
            self.sample_list.append(chr(random.randint(0, 256)))
        self.neg_list = random.sample(range(-10, 10), 10)

    def test_countingsort(self):
        result = countingsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_countingsort_neg_num(self):
        result = countingsort_neg_num(self.neg_list)
        self.assertListEqual(result, sorted(self.neg_list))

   