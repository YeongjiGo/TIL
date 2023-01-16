# deque 는 파이썬 collections 모듈에서 가지고 온다.
# queue는 데이터간 순서 관계를 유지할 수 있다.
# queue는 세 가지 기능을 가지고 있다.
# 1. 맨 뒤 데이터 추가 / 2. 맨 앞 데이터 삭제 / 3. 맨 앞 데이터 접근

from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입

queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

print(queue) # 큐 출력

# 큐의 가장 앞 데이터에 접근
print(queue[0])

# 큐의 맨 앞 데이터 삭제 및 반환
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue) # 큐 출력