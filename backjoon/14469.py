n = int(input())
li = []
for i in range(n):
    L = list(map(int,input().split()))
    li.append(L)

li.sort()

'''
[2, 1] [5, 7] [8, 3]
'''
time = 0
for i in range(n):
    if time > li[i][0]:	# 다음 소가 이전 소가 검문 받고 있는 중에 도착 했을 때
        time = time + li[i][1]	# 기다린 시간이 존재하므로 이전 소의 입장 시간 + 다음 소의 검문 시간
    else:	# 이전 소가 검문을 다 받은 후 도착 했을 때
        time = li[i][0] + li[i][1]	# 기다린 시간이 없으므로 다음 소 도착 시간 + 그 소의 검문 시간


print(time)
