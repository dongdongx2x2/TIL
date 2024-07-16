import sys
sys.stdin = open('1189_input.txt')

input = sys.stdin.readline

def dfs(x, y, dis):
    global cnt

    if x == 0 and y == c-1 and dis == k:
        cnt += 1
        return

    if ( x == 0 and y == c - 1) or dis >= k:
        return

    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy

        if 0 <= nx < r and 0 <= ny < c and not v[nx][ny] and arr[nx][ny] != 'T':
            v[nx][ny] = 1
            dfs(nx, ny, dis + 1)
            v[nx][ny] = 0


r, c, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

v = [[0] * c for _ in range(r)]
v[r-1][0] = 1

cnt = 0
dfs(r-1, 0, 1)
print(cnt)