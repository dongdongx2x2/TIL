import sys
sys.stdin = open('10819_input.txt')

input = sys.stdin.readline


def dfs(n, tlst):
    if n == N:
        sm = 0
        for i in range(N-1):
            sm += abs(tlst[i+1]-tlst[i])
        ans.append(sm)
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, tlst+[lst[j]])
            v[j] = 0

N = int(input())

lst = list(map(int,input().split()))
v = [0] * N

ans = []
dfs(0,[])

print(max(ans))
