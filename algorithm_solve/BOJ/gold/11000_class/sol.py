import sys
sys.stdin = open('11000_input.txt')

input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

cls = []
for _ in range(N):
    s, t = map(int,input().split())
    cls.append((s,t))
cls.sort()

hq = []
heappush(hq, cls[0][1])

for i in range(1, N):
    if cls[i][0] >= hq[0]:
        heappop(hq)
    heappush(hq, cls[i][1])

print(len(hq))


