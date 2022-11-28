def counting_Sort(arr, p):
    s = len(arr)
    result = [0] * s
    c = [0] * 10

    for i in range(0, s):
        index = arr[i] // p
        c[index % 10] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    i = s - 1
    while i >= 0:
        index = arr[i] // p  
        result[c[index % 10] - 1] = arr[i]
        c[index % 10] -= 1
        i -= 1
    for i in range(0, s):
        arr[i] = result[i]


def radix_Sort(arr):
    maximum = max(arr)
    p = 1
    while maximum // p > 0:
        counting_Sort(arr, p)
        p *= 10

array = [354, 954, 411, 9]
print("The original array is: ", array)
radix_Sort(array)
print("The sorted array is: ", array)