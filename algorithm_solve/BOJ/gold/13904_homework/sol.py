import sys
sys.stdin = open('13904_input.txt')

input = sys.stdin.readline

import heapq

n = int(input())

homeworks = []
for _ in range(n):
    d, w = map(int, input().split())
    homeworks.append((d,w))

homeworks.sort()
hq = []

for d,w in homeworks:
    if len(hq) < d:
        heapq.heappush(hq, w)
    else:
        heapq.heappush(hq, w)
        heapq.heappop(hq)
print(sum(hq))