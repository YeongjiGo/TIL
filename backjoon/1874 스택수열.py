import sys
n = int(sys.stdin.readline())

stack = []# 1 2 5 
ans_arr = [] # + + + + - - + + - 
new_num = 1
find = True

for i in range(n):
    num = int(sys.stdin.readline())
    while new_num <= num:
        stack.append(new_num)
        new_num +=1 #5
        ans_arr.append('+')
    if stack[-1] == num:
        ans_arr.append('-')
        stack.pop()
    else:
        find = False
        
if not find:
    print("NO")
else:
    for i in ans_arr:
        print(i)