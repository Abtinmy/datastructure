"""
    *** Time Complexity ***
    * Best case : O(N) -> sorted array
    * Worst case : O(N^2) -> reversely sorted
    * Average : O(N^2)
    
    * Space complexity = O(1)
    * In-Place sort
    * Stable sort
"""


def bubblesort(arr):
    res = arr.copy()
    for i in range(len(res)):
        for j in range(len(res) - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

def bubblesort_optimized(arr):
    res = arr.copy()
    for i in range(len(res)):
        swap = False
        for j in range(len(res) - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swap = True
        if not swap:
            return res
    return res

def bubblesort_recursion(arr):
    res = arr.copy()
    def recursive(res, index):
        if index <= 1:
            return res

        for i in range(index - 1):
            if res[i] > res[i + 1]:
                res[i], res[i + 1] = res[i + 1], res[i]
        return recursive(res, index - 1)
    return recursive(res, len(res))

def bubblesort_no_loop(arr):
    res = arr.copy()
    def recursive(res):
        if len(res) <= 1:
            return res

        if len(res) == 2:
            return res if res[0] <= res[1] else [res[1], res[0]]

        a, b = res[0], res[1]
        remain = res[2:]

        if a > b:
            return [b] + recursive([a] + remain)
        else:
            return [a] + recursive([b] + remain)
    return recursive(res)

        
#TODO: bubblesort for linked lists, using two stacks