import sys
sys.stdin = open('1743_input.txt')

input = sys.stdin.readline

def bfs(x,y):
    q = []
    q.append([x,y])
    v[x][y] = 1
    cnt = 1
    while q:

        x, y = q.pop(0)

        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <=nx < N and 0 <=ny < M and v[nx][ny] == 0 and arr[nx][ny] ==1:
                q.append([nx,ny])
                v[nx][ny] = 1
                cnt += 1
    return cnt





N, M, K = map(int, input().split())

arr = [[0]*M for _ in range(N)]
v = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

result = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            result.append(bfs(i,j))

print(max(result))
