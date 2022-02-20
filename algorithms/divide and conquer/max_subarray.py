"""
    *** Time Complexity ***
    * T(n) = 2T(n/2) + n
    * theta(n * log(n))
"""


from typing import List
import math


def max_crossing_sum(arr: List[int], left: int, mid: int, right: int) -> int:
    sum = 0
    left_sum = - math.inf
    for i in reversed(range(left, mid + 1)):
        sum += arr[i]
        if left_sum < sum:
            left_sum = sum

    sum = 0
    right_sum = - math.inf
    for i in range(mid + 1, right + 1):
        sum += arr[i]
        if right_sum < sum:
            right_sum = sum

    return max(left_sum + right_sum, left_sum, right_sum)
    
def max_subarray(arr: List[int], left: int, right: int) -> int:
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    return max(max_subarray(arr, left, mid),
               max_subarray(arr, mid + 1, right),
               max_crossing_sum(arr, left, mid, right))


# * Time Complexity : O(n)
def max_subarray_kadnae(arr: List[int]) -> int:
    res = - math.inf
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        
        if sum > res:
            res = sum
        
        if sum < 0:
            sum = 0
    
    return res
