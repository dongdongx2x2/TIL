import sys
sys.stdin = open('1486_input.txt')

def dfs(n, sum):
    global ans

    if n == N:
        if sum >= M:
            ans = min(ans, sum-M)
        return

    dfs(n+1, sum + lst[n])
    dfs(n+1, sum)

T = int(input())

for tc in range(1, T+1):

    N, M = map(int,input().split())
    lst = list(map(int,input().split()))

    ans = 10000*N
    dfs(0,0)
    print(f'#{tc} {ans}')
