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
        minimum, maximum, min_index, max_index = res[i], res[i], i, i
        for k in range(i, j + 1):
            if res[k] > maximum:
                maximum = res[k]
                max_index = k
            if res[k] < minimum:
                minimum = res[k]
                min_index = k
        res[i], res[min_index] = res[min_index], res[i]
        if res[min_index] == maximum:
            res[j], res[min_index] = res[min_index], res[j]
        else:
            res[j], res[max_index] = res[max_index], res[j]
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