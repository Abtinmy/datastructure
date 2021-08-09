"""
    *** Time Complexity ***
    * Best case : O(NlogN) -> partition always takes the middle element
    * Worst case : O(N^2) -> partition always takes the smallest or greatest element as the pivot
    * Average : O(NlogN)
    
    * Space complexity = O(1)
    * In-Place sort
    * Not Stable sort
"""


import random


#hoare partition
def partition(arr, low, high):
    pivot = arr[low]
    pivot_index = low

    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return high 

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    index = low - 1 

    for i in range(low, high):
        if arr[i] <= pivot:
            index += 1
            arr[index], arr[i] = arr[i], arr[index]
    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return index + 1

def random_partition(arr, low, high):
    pivot = random.randrange(low, high + 1)
    arr[low], arr[pivot] = arr[pivot], arr[low]
    return partition(arr, low, high)

def dual_pivot_partition(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    
    left_pivot, right_pivot = arr[low], arr[high]
    left_index = arr_index = low
    right_index = high

    while arr_index <= right_index:
        if arr[arr_index] < left_pivot:
            arr[left_index], arr[arr_index] = arr[arr_index], arr[left_index]
            left_index += 1
        elif arr[arr_index] >= right_pivot:
            while arr[right_index] > right_pivot and arr_index < right_index:
                right_index -= 1
            arr[arr_index], arr[right_index] = arr[right_index], arr[arr_index]
            right_index -= 1
            if arr[arr_index] < left_pivot:
                arr[left_index], arr[arr_index] = arr[arr_index], arr[left_index]
                left_index += 1
        arr_index += 1
    left_pivot -= 1
    right_index += 1
    arr[low], arr[left_index] = arr[left_index], arr[low]
    arr[high], arr[right_index] = arr[right_index], arr[high]
    return left_index, right_index

def quicksort(arr):
    res = arr.copy()
    def recursive(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            recursive(arr, low, pivot - 1)
            recursive(arr, pivot + 1, high)
        return arr
    return recursive(res, 0, len(res) - 1)

def lomuto_quicksort(arr):
    res = arr.copy()
    def recursive(arr, low, high):
        if low < high:
            pivot = lomuto_partition(arr, low, high)
            recursive(arr, low, pivot - 1)
            recursive(arr, pivot + 1, high)
        return arr
    return recursive(res, 0, len(res) - 1)

def random_quicksort(arr):
    res = arr.copy()
    def recursive(arr, low, high):
        if low < high:
            pivot = random_partition(arr, low, high)
            recursive(arr, low, pivot - 1)
            recursive(arr, pivot + 1, high)
        return arr
    return recursive(res, 0, len(res) - 1)

def optimized_quicksort(arr):
    res = arr.copy()
    def recursive(arr, low, high):
        while low < high:
            pivot = partition(arr, low, high)
            if pivot - low < high - pivot:
                recursive(arr, low, pivot - 1)
                low = pivot + 1
            else:
                recursive(arr, pivot + 1, high)
                high -= 1
        return arr
    return recursive(res, 0, len(res) - 1)

def stable_quicksort(arr):
    res = arr.copy()
    def recursive(arr):
        if len(arr) <= 1:
            return arr

        #middle pivoting
        middle = len(arr) // 2
        pivot = arr[middle]
        left, right = [], []

        for index, value in enumerate(arr):
            if index != middle:
                if value < pivot:
                    left.append(value)
                elif value > pivot:
                    right.append(value)
                else:
                    if index < middle:
                        left.append(value)
                    else:
                        right.append(value)
        
        return recursive(left) + [pivot] + recursive(right)

    return recursive(res)

def dual_pivot_quicksort(arr):
    res = arr.copy()
    def recursive(arr, low, high):
        if low < high:
            left_pivot, right_pivot = dual_pivot_partition(arr, low, high)
            recursive(arr, 0, left_pivot - 1)
            recursive(arr, left_pivot + 1, right_pivot - 1)
            recursive(arr, right_pivot + 1, high)
            return arr
    return recursive(res, 0, len(res) - 1)
    
 
# * Quick sort for arrays and Merge sort for linked lists.
#TODO: Quick sort for linked list, merge 2 sorted array, iterative quick sort using stack.
#TODO: Optimization with kthsmallest element