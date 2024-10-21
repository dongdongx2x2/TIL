import sys
sys.stdin = open('28353_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

p1, p2 = 0, n - 1
data.sort()
ans = 0

while p1 < p2:
    if data[p1] + data[p2] <= k:
        p1 += 1
        p2 -= 1
        ans += 1
    else:
        p2 -= 1
print(ans)
