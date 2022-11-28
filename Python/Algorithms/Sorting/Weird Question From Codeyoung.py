import time
import random

start = time.time()
arr = random.sample(range(1, 10000), 1000)
temp = arr
print(arr)
for i in range(1, 10000):
    def bubbleSort(arr):
        n = len(arr)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not swapped:
                return
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
    def insertionSort(arr):

        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):

            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    bubbleSort(arr)
    arr = temp
    print(arr, "\n")
    size = len(arr)
    shellSort(arr, size)
    arr = temp
    print(arr, "\n")
    insertionSort(arr)
    arr = temp
    print(arr, "\n")
    arr.sort()
    print(arr, "\n")
end = time.time()
total = end-start
print("total time took is:", total)
