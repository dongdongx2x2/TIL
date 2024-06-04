import sys
sys.stdin = open('1445_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs():
    v = [[[2501, 2501] for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append((start[0], start[1], 0, 0))
    v[start[0]][start[1]] = [0,0]

    while q:
        x, y, garbage, adj_garbage = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_garbage = garbage
                new_adj_garbage = adj_garbage

                if arr[nx][ny] == 'g':
                    new_garbage += 1
                elif arr[nx][ny] == '.':
                    for ddx, ddy in directions:
                        nnx, nny = nx + ddx, ny + ddy
                        if 0 <= nnx < n and 0 <= nny < m and arr[nnx][nny] == 'g':
                            new_adj_garbage += 1
                            break

                if [new_garbage, new_adj_garbage] < v[nx][ny]:
                    v[nx][ny] = [new_garbage, new_adj_garbage]
                    q.append((nx, ny, new_garbage, new_adj_garbage))

    return v[end[0]][end[1]]

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
directions = ((1,0), (-1,0), (0,1), (0,-1))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            start = (i,j)

        elif arr[i][j] == 'F':
            end = (i,j)
ans = bfs()
print(ans[0], ans[1])