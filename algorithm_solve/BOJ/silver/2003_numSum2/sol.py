import sys
sys.stdin = open('2003_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

l, r = 0, 1
cnt = 0

while r <= n and l <= r:
    sm = lst[l:r]
    total = sum(sm)

    if total == m:
        cnt += 1
        r += 1

    elif total < m:
        r += 1

    else:
        l += 1

print(cnt)