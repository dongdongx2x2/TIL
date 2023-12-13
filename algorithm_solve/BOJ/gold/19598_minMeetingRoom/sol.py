import sys
sys.stdin = open('19598_input.txt')

input = sys.stdin.readline

from heapq import heappop,heappush

n = int(input())

lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s,e))

lst.sort()

hq = []
cnt = 0

for i in lst:
    if hq and hq[0] <= i[0]:
        heappop(hq)
    heappush(hq, i[1])
    # print(hq)
    cnt = max(cnt, len(hq))
print(cnt)