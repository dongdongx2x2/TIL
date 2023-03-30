import sys
sys.stdin = open('1865_input.txt')

def check(n,s,tlst):
    global mxmx

    if s <= mxmx:
        return

    if n == N:
        mxmx = max(s,mxmx)
        return

    for j in range(N):  # 0, 1, 2
        # for k in range(N): # 0, 1, 2
        if v[j] == 0:
            v[j] = 1
            check(n+1, s*(arr[n][j]/100), tlst+[arr[n][j]])
            v[j] = 0

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    v = [0] * N

    mxmx = 0
    ans = []
    check(0,1,[])
    print(f'#{tc} {mxmx * 100:.6f}')
