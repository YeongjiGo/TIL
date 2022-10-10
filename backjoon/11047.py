n, k  = map(int,input().split())
coin = 0 
L = []
for i in range(n):
    coin = int(input())
    L.append(coin)
    
L.sort(reverse = True)

cnt = 0 #동전개수
i  = 0 #리스트 인덱스
remain = k

for i in range(len(L)):
    cnt += remain // L[i]
    remain = remain % L[i]
print(cnt)

