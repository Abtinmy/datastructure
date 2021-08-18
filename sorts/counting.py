"""
    *** Time Complexity ***
    * Best case : O(N+K) -> which K is the range of input
    * Worst case : O(N+K)
    * Average : O(N+K)
    
    * Space complexity = O(N+K)
    * Not In-Place sort
    * Stable sort
"""


def countingsort(arr):
    out = [0] * len(arr)
    count = [0] * 257 # 256 elements for 256 chars and last one for storing the size of res 

    for char in arr:
        count[ord(char)] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for i in reversed(range(1, 256)):
        count[i] = count[i - 1]

    count[0], count[256] = 0, len(arr)
    counter = 0

    for i in range(256):
        for j in range(count[i], count[i + 1]):
            out[counter] = chr(i)
            counter += 1
        if counter == len(arr):
            break
            
    return out

def countingsort_neg_num(arr):
    max_ele = max(arr)
    min_ele = min(arr)
    range_ele = max_ele - min_ele + 1

    count = [0] * range_ele
    out = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_ele] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in reversed(range(len(arr))):
        out[count[arr[i] - min_ele] - 1] = arr[i]
        count[arr[i] - min_ele] -= 1

    return out


# Using for finding mode and median of an array with limited range    
