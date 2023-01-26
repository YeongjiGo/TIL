from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    arr = list(sys.stdin.readline().split())
 
    if arr[0] == 'push':
        queue.append(arr[1])

    elif arr[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif arr[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])

    elif arr[0] == 'size':
        print(len(queue))

    elif arr[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif arr[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
