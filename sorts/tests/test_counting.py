import unittest
from sorts.counting import countingsort
import random


class TestCounting(unittest.TestCase):

    def setUp(self):
        self.sample_list = []
        for i in range(10):
            self.sample_list.append(chr(random.randint(0, 256)))

    def test_countingsort(self):
        result = countingsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

   