import random
def InsertionSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while j >=0 and temp > a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp

a = random.sample(range(20, 50), 20)
print(a)
InsertionSort(a)
print("Array after sorting:")
print(a)