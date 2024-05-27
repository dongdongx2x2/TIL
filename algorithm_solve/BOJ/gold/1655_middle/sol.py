import sys
sys.stdin = open('1655_input.txt')

input = sys.stdin.readline

import heapq

n = int(input())

min_hq = []
max_hq = []

for i in range(n):
    num = int(input())

    if len(max_hq) == len(min_hq):
        heapq.heappush(max_hq, -num)

    else:
        heapq.heappush(min_hq, num)

    if min_hq and min_hq[0] < -max_hq[0]:
        maxV = heapq.heappop(max_hq)
        minV = heapq.heappop(min_hq)

        heapq.heappush(max_hq, -minV)
        heapq.heappush(min_hq, -maxV)

    print(-max_hq[0])