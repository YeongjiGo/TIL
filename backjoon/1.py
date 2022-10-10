def func(n):
    remain = 1000-n
    li = [500, 100, 50, 10, 5, 1]
    ans = 0 #동전개수
    for i in range(len(li)):
        ans += remain // li[i]
        remain = remain % li[i]
    return ans


n = int(input())
print(func(n))