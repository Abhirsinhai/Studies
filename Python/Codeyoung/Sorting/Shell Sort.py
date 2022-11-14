def shellSort(array, a):
    gap = a // 2
    while gap > 0:
        for i in range(gap, a):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
        gap //= 2

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
print("The original array is:", array)
size = len(array)
shellSort(array, size)
print('Sorted Array is:', array)