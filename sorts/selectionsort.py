"""
    *** Time Complexity ***
    * Best case : O(N^2)
    * Worst case : O(N^2)
    * Average : O(N^2)
    
    * Space complexity = O(1)
    * In-Place sort
    * Not Stable sort
"""


def selectionsort(arr):
    res = arr.copy()
    for i in range(len(res)):
        minimum = i
        for j in range(i + 1, len(res)):
            if res[minimum] > res[j]:
                minimum = j
        res[i], res[minimum] = res[minimum], res[i]
    return res

def recursive_selectionsort(arr):
    res = arr.copy()
    def min_index(arr, start, end):
        if start == end:
            return start
        minimum = min_index(arr, start + 1, end)
        return start if arr[start] < arr[minimum] else minimum

    def recursive(arr, index):
        if index == len(arr):
            return arr
        minimum = min_index(arr, index, len(arr) - 1)
        if index != minimum:
            arr[index], arr[minimum] = arr[minimum], arr[index]
        return recursive(arr, index + 1)
    return recursive(res, 0)

#calc min and max at the same time
def optimized_selectionsort(arr):
    res = arr.copy()
    i = 0
    j = len(res) - 1
    while(i < j):
        min_index, max_index = i, i
        for k in range(i + 1, j):
            if res[k] > res[max_index]:
                max_index = k
            if res[k] < res[min_index]:
                min_index = k
        arr[i], arr[min_index] = arr[min_index], arr[i]
        arr[j], arr[max_index] = arr[max_index], arr[j]
        i += 1
        j -= 1
    return res

def stable_selectionsort(arr):
    res = arr.copy()
    for i in range(len(res)):
        minimum = i
        for j in range(i + 1, len(res)):
            if res[minimum] > res[j]:
                minimum = j
        
        #shifting
        value = res[minimum]
        while minimum > i:
            res[minimum] = res[minimum - 1]
            minimum -= 1
        res[i] = value
    return res


#TODO: Selection sort for linked lists