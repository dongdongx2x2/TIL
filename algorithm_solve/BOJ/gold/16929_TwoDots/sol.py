import sys
sys.stdin = open('16929_input.txt')

input = sys.stdin.readline

def dfs(cx, cy, px, py, cnt):
    global ans

    if v[cx][cy] and cnt >= 4:
        ans.append('TES')
        return

    v[cx][cy] = 1

    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = cx + dx, cy + dy

        if 0<=nx<n and 0<=ny<m and arr[cx][cy] == arr[nx][ny]:
            if (nx, ny) != (px, py):
                dfs(nx, ny, cx, cy, cnt + 1)


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
v = [[0] * m for _ in range(n)]

ans = []
for i in range(n):
    for j in range(m):
        if not v[i][j]:
            dfs(i,j,i,j,0)

if ans:
    print("Yes")
else:
    print("No")

