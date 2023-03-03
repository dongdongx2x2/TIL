import sys
sys.stdin = open('input.txt')


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def search(x,y):

    visited[x][y] = 1

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and G[nx][ny] != 1 and visited[nx][ny] != 1:
                if G[nx][ny] == 3:
                    return 1
                stack.append((nx, ny))
                visited[nx][ny] = 1
    return 0


for _ in range(10):
    tc = int(input())

    G = [list(map(int, input())) for _ in range(16)]

    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if G[i][j] == 2:
                x, y = i, j

    print(f'#{tc} {search(x,y)}')
