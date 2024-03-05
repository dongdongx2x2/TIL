import sys
sys.stdin = open('21921_input.txt')

input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))

mx = sum(lst[:x])
tem = mx
cnt = 1
for i in range(x, n):
    tem -= lst[i-x]
    tem += lst[i]

    if tem > mx:
        mx = tem
        cnt = 1

    elif tem == mx:
        cnt += 1

if mx == 0:
    print("SAD")
else:
    print(mx)
    print(cnt)