import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
# print(arr)

visited = [[0]*M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x,y):
    q = [(x,y)]
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if (nx+1, ny+1) == (N, M):
                    return visited[nx][ny]
print(BFS(0,0))
