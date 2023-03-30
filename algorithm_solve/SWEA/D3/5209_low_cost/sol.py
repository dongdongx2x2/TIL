import sys
sys.stdin = open('5209_input.txt')

def dfs(n, value):
    global mimi

    if mimi < value:
        return

    if n == N:
        mimi = min(mimi, value)
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, value + arr[n][j])
            v[j] = 0


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    v = [0] * N
    mimi = 100*16
    dfs(0,0)
    print(f'#{tc} {mimi}')
