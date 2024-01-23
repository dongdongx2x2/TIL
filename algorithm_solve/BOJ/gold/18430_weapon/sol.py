import sys
sys.stdin = open('18430_input.txt')

input = sys.stdin.readline

def dfs(i, j, sum):
    global mx

    # 열부터 탐색
    if j == m:
        i += 1
        j = 0
    # 끝 도달 시 종료
    if i == n:
        mx = max(mx, sum)
        return

    if not visited[i][j]:
        for k in range(4):
            a, b, c, d = shape[k]
            x, y, xx, yy = i + a, j + b, i + c, j + d
            if 0 <= x < n and 0 <= xx < n and 0 <= y < m and 0 <= yy < m and not visited[x][y] and not visited[xx][yy]:
                visited[x][y] = visited[xx][yy] = visited[i][j] = True
                dfs(i, j + 1, sum + board[i][j] * 2 + board[x][y] + board[xx][yy])
                visited[x][y] = visited[xx][yy] = visited[i][j] = False
    dfs(i, j + 1, sum)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

shape = {0: [0, -1, 1, 0], 1: [-1, 0, 0, -1], 2: [-1, 0, 0, 1], 3: [0, 1, 1, 0]}
# 0: 왼쪽, 아래, 1: 위쪽 왼쪽, 2 : 위쪽 오른쪽, 3: 오른쪽 아래
visited = [[False] * m for _ in range(n)]
mx = 0
dfs(0, 0, 0)
print(mx)
