def Counting_Sort(arr):
    s = len(arr)
    result = [0] * s
    count = [0] * 10
    
    for i in range(0, s):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = s - 1
    while i >= 0:
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, s):
        arr[i] = result[i]

#driver code
array = [9, 8, 4, 5, 8, 9, 3, 2, 3, 1]
print("The original array is: ", array)
Counting_Sort(array)
print("Array after sorting is: ", array)