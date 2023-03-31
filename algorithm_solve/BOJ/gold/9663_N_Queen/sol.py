import sys
sys.stdin = open('9663_input.txt')

input = sys.stdin.readline


def dfs(n):
    global cnt

    if n == N:
        cnt += 1
        return

    for j in range(N):
        if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0:
            v1[j] = 1
            v2[n+j] = 1
            v3[n-j] = 1
            dfs(n+1)
            v1[j] = 0
            v2[n+j] = 0
            v3[n-j] = 0


N = int(input())

v1 = [0] * N
v2 = [0] * (N*2)
v3 = [0] * (N*2)

cnt = 0

dfs(0)

print(cnt)