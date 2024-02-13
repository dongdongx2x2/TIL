import sys
sys.stdin = open('1202_input.txt')

input = sys.stdin.readline

from collections import deque
import heapq

n, k = map(int, input().split())
jewels = deque(sorted([list(map(int, input().split())) for _ in range(n)]))
bags = sorted([int(input()) for _ in range(k)])

hq = []
res = 0

for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(hq, -jewels[0][1])
        jewels.popleft()
    if hq:
        res -= heapq.heappop(hq)
    elif not jewels:
        break

print(res)