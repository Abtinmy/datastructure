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
    res = arr.copy()
    out = [0] * len(res)
    count = [0] * 257 # 256 elements for 256 chars and last one for storing the size of res 

    for char in arr:
        count[ord(char)] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for i in reversed(range(1, 256)):
        count[i] = count[i - 1]

    count[0], count[256] = 0, len(res)
    counter = 0

    for i in range(256):
        for j in range(count[i], count[i + 1]):
            out[counter] = chr(i)
            counter += 1
        if counter == len(res):
            break
            
    return out

    
#TODO: Stable counting sort, support negative numbers