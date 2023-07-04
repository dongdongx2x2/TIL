import sys
sys.stdin = open("1976_input.txt")

input = sys.stdin.readline

from collections import deque

def bfs(n):

    q = deque()
    q.append(n)
    v[lst[0]] = 1

    while q:
        cn = q.popleft()

        for j in range(N):
            if arr[cn-1][j] == 1 and v[j+1] == 0:
                q.append(j+1)
                v[j+1] = 1


N = int(input())
M = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

lst = list(map(int,input().split()))

v = [0] * (N+1)
bfs(lst[0])
# print(v)
cnt = 0
for i in lst:
    if v[i] != 0:
        cnt += 1

if cnt == len(lst):
    print('YES')
else:
    print('NO')