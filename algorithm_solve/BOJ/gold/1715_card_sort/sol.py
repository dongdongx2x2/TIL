import sys
sys.stdin = open('1715_input.txt')

input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input())

lst = []

for _ in range(N):
    heappush(lst,int(input()))

if len(lst) == 1:
    print(0)

else:
    result = 0
    while 1 < len(lst):
        tem = heappop(lst) + heappop(lst)
        result += tem
        heappush(lst,tem)
    print(result)