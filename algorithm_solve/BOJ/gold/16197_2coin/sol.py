import sys
sys.stdin = open('16197_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(coin):
    q = deque([(coin, 0)])
    v = set([coin])

    while q:
        (cx1, cy1, cx2, cy2), cnt = q.popleft()

        if cnt >= 10:
            return -1

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx1, ny1 = cx1 + dx, cy1 + dy
            nx2, ny2 = cx2 + dx, cy2 + dy

            if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:
                if arr[nx1][ny1] == "#":
                    nx1, ny1 = cx1, cy1
                if arr[nx2][ny2] == "#":
                    nx2, ny2 = cx2, cy2
                if (nx1, ny1, nx2, ny2) not in v:
                    v.add((nx1, ny1, nx2, ny2))
                    q.append(((nx1, ny1, nx2, ny2), cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m and not (0 <= nx2 < n and 0 <= ny2 < m):
                return cnt + 1
            elif not (0 <= nx1 < n and 0 <= ny1 < m) and 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1

    return -1


n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

coin = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'o':
            coin.append(i)
            coin.append(j)

coin = tuple(coin)
print(bfs(coin))