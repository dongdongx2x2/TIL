import sys

sys.stdin = open('16206_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(key=lambda x: (x % 10,x))

ans = 0
for cake in lst:
    cnt = cake // 10
    if cake % 10 == 0:
        if cnt-1 <= m:
            ans += cnt
            m -= cnt-1
        else:
            ans += m
            m = 0
    else:
        if cnt <= m:
            ans += cnt
            m -= cnt

        else:
            ans += m
            m = 0
print(ans)

