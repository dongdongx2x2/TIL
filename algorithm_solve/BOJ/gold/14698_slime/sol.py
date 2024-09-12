import sys
sys.stdin = open('14698_input.txt')

input = sys.stdin.readline
import heapq

def solve(lst):
    if len(lst) == 1:
        return 1

    heapq.heapify(lst)

    total_cost = 1
    while len(lst) > 1:
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)
        cost = a * b
        total_cost = (total_cost * cost) % 1000000007
        heapq.heappush(lst, a*b)

    return total_cost

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = solve(lst)
    print(ans)