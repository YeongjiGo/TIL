11001100110011000001

1 :9개
0 : 11개

1) 1이랑 0 갯수 카운트 후 비교해서 적은 쪽 숫자를 많은 숫자로 바꾼다



n = input()

cnt0 =0
cnt1= 0
for i in n:
    if i == '0':
        cnt0 +=1
    else:
        cnt1 +=1


if cnt0 > cnt1:
    