import sys
sys.stdin = open('3980_input.txt')

input = sys.stdin.readline

def dfs(cnt, sm):
    global mxmx

    if cnt == 11:
        mxmx = max(mxmx, sm)
        return

    for i in range(11):
        if v[i] or arr[cnt][i] == 0:
            continue

        v[i] = 1
        dfs(cnt + 1, sm + arr[cnt][i])
        v[i] = 0

c = int(input())

for _ in range(c):
    arr = [list(map(int, input().split())) for _ in range(11)]
    v = [0] * 11

    mxmx = 0

    dfs(0,0)
    print(mxmx)