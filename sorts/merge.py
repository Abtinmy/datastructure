"""
    *** Time Complexity ***
    * Best case : O(NlogN) 
    * Worst case : O(NlogN)
    * Average : O(NlogN)
    
    * Space complexity = O(n)
    * Not In-Place sort
    * Stable sort
"""


def mergesort(arr):
    res = arr.copy()
    def recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        recursive(left)
        recursive(right)
        left_index = right_index = arr_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                arr[arr_index] = left[left_index]
                left_index += 1
            else:
                #number of inversions can be calculated here
                arr[arr_index] = right[right_index]
                right_index += 1
            arr_index += 1
        
        while left_index < len(left):
            arr[arr_index] = left[left_index]
            arr_index += 1
            left_index += 1
        
        while right_index < len(right):
            arr[arr_index] = right[right_index]
            arr_index += 1
            right_index += 1
        
        return arr
    return recursive(res)

def inplace_mergesort(arr):
    res = arr.copy()
    max_val = max(res) + 1
    def merge(arr, start, middle, finish):
        left_index, right_index, arr_index = start, middle + 1, start

        while left_index <= middle and right_index <= finish:
            if arr[left_index] % max_val <= arr[right_index] % max_val:
                arr[arr_index] = arr[arr_index] + (arr[left_index] % max_val) * max_val
                arr_index += 1
                left_index +=1
            else :
                arr[arr_index] = arr[arr_index] + (arr[right_index] % max_val) * max_val
                arr_index += 1
                right_index +=1
        
        while left_index <= middle:
            arr[arr_index] = arr[arr_index] + (arr[left_index] % max_val) * max_val
            arr_index += 1
            left_index += 1
        
        while right_index <= finish:
            arr[arr_index] = arr[arr_index] + (arr[right_index] % max_val) * max_val
            arr_index += 1
            right_index += 1
        
        for i in range(start, finish - 1):
            arr[i] = arr[i] // max_val
        return arr
            

    def recursive(arr, start, finish):
        if start < finish :
            middle = (start + finish) // 2
            recursive(arr, start, middle)
            recursive(arr, middle + 1, finish)
            merge(arr, start, middle, finish)
            return arr
    return recursive(res, 0, len(res) - 1)

def inplace_shifiting_mergesort(arr):
    res = arr.copy()
    def merge(arr, start, middle, finish):
        left_index, right_index, arr_index = start, middle + 1, start

        if arr[middle] <= arr[right_index]:
            return arr

        while left_index <= middle and right_index <= finish:
            if arr[left_index] <= [right_index]:
                left_index +=1
            else :
                val = arr[right_index]
                index = right_index
                while index != left_index:
                    arr[index] = arr[index - 1]
                    index -= 1

                arr[left_index] = val
                left_index += 1
                right_index += 1
                arr_index += 1        
       
        return arr
            
    def recursive(arr, start, finish):
        if start < finish :
            middle = (start + finish) // 2
            recursive(arr, start, middle)
            recursive(arr, middle + 1, finish)
            merge(arr, start, middle, finish)
            return arr
    return recursive(res, 0, len(res) - 1)

#TODO: Linked lists.