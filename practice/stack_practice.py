from collections import deque

stack = deque()

# 스택 맨 끝에 데이터 추가

stack.append("h")
stack.append("e")
stack.append("l")
stack.append("l")
stack.append("o")

print(stack) # 스택 출력

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack) # 스택 출력