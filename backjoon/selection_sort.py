arr = [4, 2, 3, 9, 5, 7]
index, temp = 0, 0
for i in range(5):
    min = 999
    for j in range(i, 5):
        if min > arr[j]:
            min = arr[j]
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp
    print(arr)
for i in arr:
    print(i, end = ' ')