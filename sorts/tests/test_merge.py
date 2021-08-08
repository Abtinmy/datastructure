import unittest
from sorts.merge import (
    mergesort,
    inplace_mergesort,
    inplace_shifiting_mergesort
)
import random


class TestMerge(unittest.TestCase):

    def __generate_worst_case(self, arr, start, finish):
        if start < finish:
            middle = (start + finish) // 2
            left, right = arr[0::2], arr[1::2]
            self.__generate_worst_case(left, start, middle)
            self.__generate_worst_case(right, middle + 1, finish)
            for i in range(middle - start + 1):
                arr[i] = left[i]
            for j in range(finish - middle):
                arr[middle - start + 1 + j] = right[j]
            
    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)
        self.worst_case = [i for i in range(1, 17)]
        self.__generate_worst_case(self.worst_case, 0, len(self.worst_case) - 1)

    def test_mergesort(self):
        result = mergesort(self.sample_list)
        result_worst_case = mergesort(self.worst_case)
        self.assertListEqual(result, sorted(self.sample_list))
        self.assertListEqual(result_worst_case, sorted(self.worst_case))

    def test_inplace_mergesort(self):
        result = inplace_mergesort(self.sample_list)
        result_worst_case = mergesort(self.worst_case)
        self.assertListEqual(result, sorted(self.sample_list))
        self.assertListEqual(result_worst_case, sorted(self.worst_case))
    
    def test_inplace_shifiting_mergesort(self):
        result = inplace_shifiting_mergesort(self.sample_list)
        result_worst_case = mergesort(self.worst_case)
        self.assertListEqual(result, sorted(self.sample_list))
        self.assertListEqual(result_worst_case, sorted(self.worst_case))


    