def countingsort(arr):
    res = arr.copy()
    out = [0] * len(res)
    count = [0] * 256

    for char in arr:
        count[ord(char)] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for i in reversed(range(1, 256)):
        count[i] = count[i - 1]

    count[0] = 0
    counter = 0

    for i in range(256):
        if i == 255:
            for j in range(count[i], len(res)):
                 out[counter] = chr(i)
                 counter += 1
        else:
            for j in range(count[i], count[i + 1]):
                out[counter] = chr(i)
                counter += 1
        if counter == len(res):
            break
            
    return out
    