##5 2
##3 1 2 5 4
##0 1 2 3 4

n,k = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
tmp, index = 0, 0

for i in range(n-1,-1, -1):
    max = -100
    
    for j in range(0, i+1):
        if max < arr[j]:
            max = arr[j]
            index = j
        
    tmp = arr[i]
    arr[i] = arr[index]
    arr[index] = tmp
    for i in range(n):
        testarr[i] = arr[i]

    for i in range(n):

    if cnt == k:
        print(arr)
