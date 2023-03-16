import sys
sys.stdin = open('15657_input.txt')

input = sys.stdin.readline

def dfs(n,tlst):

    if n == M:
        ans.append(tlst)
        return

    for j in range(N):
        if (not tlst) or tlst[-1] <= lst[j]:
            dfs(n+1, tlst + [lst[j]])


N, M = map(int, input().split())

lst = sorted(list(map(int, input().split())))

ans = []

dfs(0, [])

for i in ans:
    print(*i)