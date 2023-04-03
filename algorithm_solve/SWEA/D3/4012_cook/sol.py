import sys
sys.stdin = open('4012_input.txt')

def dfs(n, alst, blst):
    global mimi

    if n == N:
        if len(alst) == N//2:
            sum1 = 0
            sum2 = 0
            for i in range(N//2):
                for j in range(N//2):
                    sum1 += arr[alst[i]][alst[j]]
                    sum2 += arr[blst[i]][blst[j]]
            mimi = min(mimi, abs(sum1-sum2))
        return

    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    mimi = 99999999
    dfs(0, [], [])
    print(f'#{tc} {mimi}')
