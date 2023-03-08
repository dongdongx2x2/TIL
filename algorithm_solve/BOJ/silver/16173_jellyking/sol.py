import sys
sys.stdin = open('16173_input.txt')

input = sys.stdin.readline

def bfs():
    v = [[0]*N for _ in range(N)]

    dx = [0, 1]  # 우 하
    dy = [1, 0]

    x = y= 0
    q = []
    q.append((x,y))

    while q:
        cx,cy = q.pop(0)

        if arr[cx][cy] == -1:
            return 'HaruHaru'

        for i in range(2):
            nx = cx + dx[i] * arr[cx][cy]
            ny = cy + dy[i] * arr[cx][cy]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx,ny))

    return 'Hing'

N = int(input())

arr = [list(map(int, input().split()))for _ in range(N)]

print(bfs())


