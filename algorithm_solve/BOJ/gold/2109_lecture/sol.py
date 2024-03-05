import sys, heapq
sys.stdin = open('2109_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    p, d = map(int, input().split())
    lst.append((p,d))


lst.sort(key=lambda x:(x[1],-x[0]))
# print(lst)

hq = []

for p, d in lst:
    heapq.heappush(hq, p)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))
