"""
    *** Time Complexity ***
    * Best case : O(N) -> Sorted Array
    * Worst case : O(N^2) -> Reversed order
    * Average : O(N^2)
    
    * Space complexity = O(1)
    * In-Place sort
    * Stable sort
"""


def insertionsort(arr):
    res = arr.copy()
    for i in range(1, len(res)):
        val = res[i]
        j = i - 1
        while j >= 0 and res[j] > val: #it also can be implemented with swapping
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = val
    return res

def recursive_insertionssort(arr):
    res = arr.copy()
    def recursive(res, index):
        if index <= 1:
            return res
        recursive(res, index - 1)
        j = index - 2
        val = res[index - 1]
        while j >= 0 and res[j] > val:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = val
    return recursive(res, len(res))

#Insertion sort to sort even and odd positioned elements in different orders
#Input : [5, 8, 4, 3, 9, 2, 7, 9, 1]
#Output : [1, 8, 4, 6, 5, 2, 7, 3, 9]
def insertionsort_even_odd(arr):
    res = arr.copy()
    for i in range(2, len(res)):
        j = i - 2
        val = res[i]
        if j % 2 == 0:
            while j >= 0 and res[j] > val:
                res[j + 2] = res[j]
                j -= 2
            res[j + 2] = val
        else:
            while j >= 0 and res[j] < val:
                res[j + 2] = res[j]
                j -= 2
            res[j + 2] = val
    return res


#TODO: Binary insertion sort, for linked lists.