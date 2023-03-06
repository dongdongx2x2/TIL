import sys
sys.stdin = open('9490_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for x in range(N):
        for y in range(M):
            cnt = arr[x][y]

            dx = [-1,1,0,0]
            dy = [0,0,1,-1]

            for i in range(4):
                for m in range(1, arr[x][y]+1):
                    nx = x + dx[i]*m
                    ny = y + dy[i]*m

                    if 0 <= nx < N and 0 <= ny < M:
                        cnt += arr[nx][ny]
            mx = max(cnt, mx)
    print(f'#{tc} {mx}')
