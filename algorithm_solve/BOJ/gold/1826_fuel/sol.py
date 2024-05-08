import sys
sys.stdin = open('1826_input.txt')

input = sys.stdin.readline

import heapq

n = int(input())

lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))

l, p = map(int, input().split())
lst.append((l, 0))

lst.sort()

hq = []
cur = 0
stop = 0

for dist, fuel in lst:
    while p < dist - cur:
        if not hq:
            print(-1)
            exit()

        p += -heapq.heappop(hq)
        stop += 1

    p -= dist - cur
    cur = dist
    heapq.heappush(hq, -fuel)
print(stop)
