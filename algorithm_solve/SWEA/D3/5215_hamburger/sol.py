import sys
sys.stdin = open('5215_input.txt')

def dfs(n, sm, tst):
    global taste

    if sm > L:
        return

    if n == N:
        taste = max(tst, taste)
        return

    dfs(n+1, sm+lst[n][1], tst+lst[n][0])
    dfs(n+1, sm, tst)


T = int(input())

for tc in range(1, T+1):

    N, L = map(int, input().split())

    lst = []
    for _ in range(N):
        lst.append(list(map(int ,input().split())))

    taste = 0

    dfs(0, 0, 0)
    print(f'#{tc} {taste}')
