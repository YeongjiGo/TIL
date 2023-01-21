import sys

n = int(input())
stack = []

for i in range(n):
    arr = list(sys.stdin.readline().split())
    if arr[0] == 'push':
        stack.append(arr[1])
        
    elif arr[0] == 'top':
        if not stack: #리스트가 비어 있으면
            print(-1)
        else:
            print(stack[len(stack)-1])
            
    elif arr[0] == 'size':
        print(len(stack))
        
    elif arr[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1) #비어있으면
            
    elif arr[0] == 'pop':
        if not stack: # 비어있으면
            print(-1)
        else:
            print(stack.pop())
