import unittest
from sorts.shell import shellsort
import random


class TestQuick(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)

    def test_shellsort(self):
        result = shellsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    