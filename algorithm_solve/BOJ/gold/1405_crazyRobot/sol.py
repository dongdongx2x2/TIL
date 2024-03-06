import sys
sys.stdin = open('1405_input.txt')

input = sys.stdin.readline

def dfs(x, y, cnt, prob):
    global ans

    if cnt == N:
        ans += prob
        return

    v[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if v[nx][ny] == 0:
            dfs(nx, ny, cnt + 1, prob * dir_prob[i])

    v[x][y] = 0


N, ep, wp, sp, np = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dir_prob = [ep/100, wp/100, sp/100, np/100]

v = [[0] * 29 for _ in range(29)]

ans = 0
dfs(14, 14, 0, 1)

print(ans)