n = int(input())

for i in range(n):
    s = input()
    cnt = 0
    for j in s:

        if j == '(':
            cnt +=1
        elif j == ')':
            cnt -=1
        if cnt <0 : # )로 시작하면
            print('NO')
            break
                
        
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
