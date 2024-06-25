import sys
sys.stdin = open('15565_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
cnt = 0
min_len = int(1e9)

for right in range(n):
    if lst[right] == 1:
        cnt += 1

    while cnt >= k:
        min_len = min(min_len, right - left + 1)
        if lst[left] == 1:
            cnt -= 1
        left += 1

if min_len == int(1e9):
    print(-1)
else:
    print(min_len)
