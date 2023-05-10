import sys
sys.stdin = open('1374_input.txt')

input = sys.stdin.readline
from heapq import heappop,heappush

N = int(input())

lst = []

for _ in range(N):
    __, s, e = map(int,input().split())
    lst.append((s,e))
# lst.sort()
lst.sort()
# print(lst)

hq = []
cnt = 0

for i in lst:
    while hq and hq[0] <= i[0]:
        heappop(hq)
    heappush(hq, i[1])
    cnt = max(cnt, len(hq))

print(cnt)