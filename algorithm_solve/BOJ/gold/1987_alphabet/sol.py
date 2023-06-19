import sys
sys.stdin = open('1987_input.txt')

input = sys.stdin.readline

def dfs(cx, cy, cnt):
    global ans
    ans = max(ans, cnt)

    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < R and 0 <= ny < C and v[ord(arr[nx][ny])] == 0:
            v[ord(arr[nx][ny])] = 1
            dfs(nx, ny, cnt + 1)
            v[ord(arr[nx][ny])] = 0

R, C = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(R)]

ans = 1
v = [0] * 128
v[ord(arr[0][0])] = 1
dfs(0,0,1)

print(ans)


