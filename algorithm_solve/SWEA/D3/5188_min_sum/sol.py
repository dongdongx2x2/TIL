import sys
sys.stdin = open('5188_input.txt')

def check(x,y):
        global result, mimi

        v[x][y] = 1
        dx = [0, 1]  #오른쪽, 밑
        dy = [1, 0]

        if result > mimi:
            return

        if x == N-1 and y == N-1:
            mimi = result
            return

        for i in range(2):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0:
                v[nx][ny] = 1
                result += arr[nx][ny]
                check(nx,ny)
                v[nx][ny] = 0
                result -= arr[nx][ny]


T = int(input())

for tc in range(1,T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    mimi = 13* 100
    result = arr[0][0]
    v = [[0] * N for _ in range(N)]

    check(0,0)

    print(f'#{tc} {mimi}')