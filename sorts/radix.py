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
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        index = arr[i] / dig
        out[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(len(arr)):
        arr[i] = out[i]

def radixsort(arr):
    res = arr.copy()
    max_ele = max(res)
    dig = 1

    while max_ele / dig > 0:
        countingsort(res, dig)
        dig *= 10

def msd_radixsort(arr):
    res = arr.copy()
    def recursion(arr, low, high, dig):
        if high <= low:
            return

        out = [0] * len(arr)
        count = [0] * 10 

        for num in arr:
            index = int(str(num)[dig])
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            index = int(str(num)[dig])
            out[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(len(arr)):
            arr[i] = out[i]

        for i in range(9):
            recursion(res, low + count[i], low + count[i + 1] - 1, dig + 1)
        return res
    return recursion(res, 0, len(res) - 1, 0)


#TODO: inplace, trie