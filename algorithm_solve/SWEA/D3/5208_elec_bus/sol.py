import sys
sys.stdin = open('5208_input.txt')

def dfs(n,cnt):
    global mimi


    if mimi <= cnt:
        return

    if n == N-1:
        mimi = min(mimi,cnt)
        return

    for j in range(1, lst[n]+1):
        dfs(n+j, cnt+1)

T = int(input())

for tc in range(1, T+1):

    lst = list(map(int, input().split()))
    N = lst[0]
    lst = lst[1:]

    mimi = 101

    dfs(0,0)

    print(f'#{tc} {mimi-1}')
