import sys
sys.stdin = open('11286_input.txt')

input = sys.stdin.readline

from heapq import heappop,heappush

N = int(input())

hq = []

for _ in range(N):
    a = int(input())

    if a != 0:
        heappush(hq, (abs(a),a))

    else:
        if hq:
            print(heappop(hq)[1])
        else:
            print(0)
