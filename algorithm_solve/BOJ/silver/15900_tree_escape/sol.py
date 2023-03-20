import sys
sys.stdin = open('15900_input.txt')
input = sys.stdin.readline

from collections import deque

N = int(input())

arr = [[] for _ in range(N+1)]
p = [0] * (N+1)
p[1] = 1

dis = [0] * (N+1)

for _ in range(N-1):

    s, e = map(int, input().split())

    arr[s].append(e)
    arr[e].append(s)

def bfs(arr):
    q = deque([])
    q.append(1)

    while q:
        start = q.popleft()

        for n in arr[start]:
            if p[n] == 0:
                p[n] = start
                dis[n] = dis[start] + 1
                q.append(n)

bfs(arr)
# print(p)
# print(dis)
# print(arr)
result = 0
for i in range(2, N+1):
    if len(arr[i]) == 1:
        result += dis[i]

if result % 2:
    print('Yes')
else:
    print('No')