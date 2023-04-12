import sys
sys.stdin = open('11279_input.txt')

input = sys.stdin.readline

from heapq import heappop,heappush

N = int(input())

lst = []

for _ in range(N):
    a = int(input())

    if a == 0:
        if lst:
            print(-heappop(lst))
        else:
            print(0)
    else:
        heappush(lst,-a)