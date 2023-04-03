import sys
sys.stdin = open('1260_input.txt')

from collections import deque

def dfs(i):
    v[i] = 1
    print(i,end=' ')
    for w in arr[i]:
        if v[w] == 0:
            dfs(w)

def bfs(i):
    q = deque()
    q.append(i)
    v2[i] = 1

    while q:
        x = q.popleft()
        print(x, end=' ')

        for w in arr[x]:
            if v2[w] == 0:
                v2[w] = 1
                q.append(w)



N, M, V = map(int, input().split())

arr = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int,input().split())

    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

v = [0] * (N+1)
v2 = [0] * (N+1)
dfs(V)
print()
bfs(V)