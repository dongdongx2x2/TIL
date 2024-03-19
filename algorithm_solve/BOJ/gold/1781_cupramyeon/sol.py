import sys
sys.stdin = open('1781_input.txt')

input = sys.stdin.readline

import heapq

n = int(input())

homeworks = []

for _ in range(n):
    d, c = map(int, input().split())
    homeworks.append((d, c))

homeworks.sort()

hq = []

for homework in homeworks:
    d, c = homework

    heapq.heappush(hq, c)
    if len(hq) > d:
        heapq.heappop(hq)
    # print(hq)
print(sum(hq))