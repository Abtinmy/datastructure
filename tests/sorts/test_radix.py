import unittest
from sorts.radix import (
    radixsort,
    msd_radixsort
)
import random


class TestRadix(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)

    def test_radixsort(self):
        result = radixsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

    def test_msd_radixsort(self):
        result = msd_radixsort(self.sample_list)
        self.assertListEqual(result, sorted(self.sample_list))

   