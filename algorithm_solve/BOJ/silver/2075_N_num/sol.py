import sys
sys.stdin = open('2075_input.txt')

input = sys.stdin.readline

from heapq import heappop, heappush,heapify

N = int(input())

hq = []

for _ in range(N):
    lst = list(map(int, input().split()))
    if not hq:
        hq = lst
        heapify(hq)

    else:
        for n in lst:
            if hq[0] < n:
                heappush(hq,n)
                heappop(hq)

print(hq[0])

