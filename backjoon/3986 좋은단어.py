import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    word = sys.stdin.readline().strip()
    stack = []
    for j in word:
        if stack: # 데이터가 들어있으면
            if j == stack[-1]:
                stack.pop()
                
            else:
                stack.append(j)
        else:
            stack.append(j)
    if not stack:
        cnt +=1
print(cnt)
    