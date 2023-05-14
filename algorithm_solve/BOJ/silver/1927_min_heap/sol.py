import sys
sys.stdin = open('1927_input.txt')

input = sys.stdin.readline

from heapq import heappop,heappush


N = int(input())

hq = []

for _ in range(N):
    a = int(input())

    if a == 0:
        if hq:
            print(heappop(hq))
        else:
            print(0)
    else:
        heappush(hq,a)
