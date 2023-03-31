import sys
sys.stdin = open('2817_input.txt')

def dfs(n, sm):
    global ans

    if sm > K:
        return

    if n == N:
        if sm == K:
            ans += 1
        return

    dfs(n+1, sm + lst[n])
    dfs(n+1, sm)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    lst = list(map(int, input().split()))

    ans = 0

    dfs(0,0)

    print(f'#{tc} {ans}')