"""
    *** Time Complexity ***
    
    -- d is number of digits and b is the base

    * Best case : O(dN) -> when all numbers have the same number of digits
    * Worst case : O((D*(N+b)) -> when all numbers have the same number of digits
                                except one element which has large number of digits
    * Average : O(D*(N+b))
    
    * Space complexity = O(N+b)
    * Not In-Place sort
    * Stable sort
"""


def countingsort(arr, dig):
    out = [0] * len(arr)
    count = [0] * 10 

    for num in arr:
        index = num / dig
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        index = arr[i] / dig
        out[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1

    for i in range(len(arr)):
        arr[i] = out[i]

def radixsort(arr):
    res = arr.copy()
    max_ele = max(res)
    dig = 1

    while max_ele / dig > 0:
        countingsort(res, dig)
        dig *= 10

    return res

def nth_digit(number, digit, max_dig):
    str_num = str(number)
    return int(str_num[len(str_num) - max_dig + digit]) if max_dig <= len(str_num) + digit else 0

#most significant digit
def msd_radixsort(arr):
    res = arr.copy()
    max_dig = len(str(max(res)))
    def recursion(arr, low, high, dig):
        if high <= low:
            return

        out = [0] * len(arr)
        count = [0] * 11 # one extra for number 1 digit

        for i in range(low, high + 1):
            index = nth_digit(arr[i], dig, max_dig)
            count[int(index)] += 1

        for i in range(1, 11):
            count[i] += count[i - 1]

        for i in range(low, high + 1):
            index = nth_digit(arr[i], dig, max_dig)
            out[count[int(index)] - 1] = arr[i]
            count[int(index)] -= 1

        for i in range(low, high + 1):
            arr[i] = out[i - low]

        for i in range(10):
            recursion(arr, low + count[i], low + count[i + 1] - 1, dig + 1)
        return arr
    return recursion(res, 0, len(res) - 1, 0)


#TODO: inplace, trie, linked list