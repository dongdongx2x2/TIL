import sys
sys.stdin = open('15655_input.txt')

input = sys.stdin.readline


def dfs(n, tlst):

    if n == M:
        ans.append(tlst)
        return

    for j in range(N):
        if v[j] == 0 and (not tlst or tlst[-1] < lst[j]):
            v[j] = 1
            dfs(n+1, tlst + [lst[j]])
            v[j] = 0


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

v = [0]*(N+1)
ans = []

dfs(0, [])

for i in ans:
    print(*i)