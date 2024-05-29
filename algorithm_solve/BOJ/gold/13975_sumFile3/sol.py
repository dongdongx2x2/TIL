import sys
sys.stdin = open('13975_input.txt')

input = sys.stdin.readline

import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    lst = list(map(int, input().split()))

    heapq.heapify(lst)

    ans = 0

    while len(lst) > 1:
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)
        tem = a + b
        ans += tem

        heapq.heappush(lst, tem)

    print(ans)