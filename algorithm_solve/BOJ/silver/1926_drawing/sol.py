import sys
sys.stdin = open('1926_input.txt')

input = sys.stdin.readline


def dfs(x,y):

    stack = []
    stack.append((x,y))
    v[x][y] = 1
    area = 1

    while stack:
        cx, cy = stack.pop()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and arr[nx][ny] == 1:
                v[nx][ny] = 1
                stack.append((nx,ny))
                area += 1
    return area




n, m = map(int,input().split())


v = [[0] * m for _ in range(n)]

arr = [list(map(int,input().split())) for _ in range(n)]


cnt = 0
mxmx = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == 0:
            mxmx = max(mxmx, dfs(i,j))
            cnt += 1

print(cnt)
print(mxmx)