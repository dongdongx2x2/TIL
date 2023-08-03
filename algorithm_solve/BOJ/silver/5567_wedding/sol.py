import sys
sys.stdin = open('5567_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(a):
    v[a] = 1

    q = deque()
    q.append(a)

    while q:
        ca = q.popleft()

        for j in arr[ca]:
            if v[j] == 0:
                v[j] = v[ca] + 1
                q.append(j)


n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

v = [0] * (n+1)

bfs(1)

cnt = 0
for i in v:
    if 1 < i <= 3:
        cnt += 1
print(cnt)