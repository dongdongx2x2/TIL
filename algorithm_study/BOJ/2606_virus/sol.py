import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N  = int(input()) # 컴퓨터 수

E = int(input()) # 간선 수

mat = [[0] * (N+1) for _ in range(N+1)]

for i in range(E):
    x, y = map(int, input().split()) # 연결된 간선 2차원 배열에 표시하기
    mat[x][y] = 1
    mat[y][x] = 1

visited = [0] * (N+1)

def BFS(now):
    q = [now]
    visited[now] = 1

    while q:
        now = q.pop(0)
        for next in range(1, N+1):
            if mat[now][next] == 1 and visited[next] ==0:
                q.append(next)
                visited[next] = 1
    return visited.count(1) - 1

print(BFS(1))

