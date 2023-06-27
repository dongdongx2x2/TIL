import sys

sys.stdin = open('14500_input.txt')

input = sys.stdin.readline


def dfs(x, y, depth, sm):
    global mx

    if depth == 4:
        mx = max(mx, sm)
        return

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0:
            if depth == 2:
                v[nx][ny] = 1
                dfs(x, y, depth + 1, sm + arr[nx][ny])
                v[nx][ny] = 0
            v[nx][ny] = 1
            dfs(nx, ny, depth + 1, sm + arr[nx][ny])
            v[nx][ny] = 0


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
# 나머지는 백트래킹 그냥

# ㅗ 이모양 백트래킹 안의 백트래킹,,,
mx = 0

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        v[i][j] = 0
print(mx)
