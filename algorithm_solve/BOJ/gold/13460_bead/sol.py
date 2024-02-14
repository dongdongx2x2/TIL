import sys
sys.stdin = open('13460_input.txt')

input = sys.stdin.readline

from collections import deque

def move(x, y, dx, dy):
    cnt = 0
    while arr[x + dx][y + dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    v = set()
    v.add((rx,ry,bx,by))
    q = deque()
    q.append((rx,ry,bx,by,0))

    while q:
        crx, cry, cbx, cby, depth = q.popleft()

        if depth >= 10:
            return -1

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nrx, nry, rcnt = move(crx,cry,dx,dy)
            nbx, nby, bcnt = move(cbx,cby,dx,dy)

            if arr[nbx][nby] != 'O':
                if arr[nrx][nry] == 'O':
                    return depth + 1

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx
                        nry -= dy

                    else:
                        nbx -= dx
                        nby -= dy

                if (nrx, nry, nbx, nby) not in v:
                    v.add((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby, depth + 1))
    return -1

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

print(bfs())



