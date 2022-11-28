list = []
for i in range(10):
    x = int(input("Please enter a number: "))
    list.append(x)

print("Original List: ", list)
Fixed = set(list)
print("List after removing duplicate elements: ", Fixed)