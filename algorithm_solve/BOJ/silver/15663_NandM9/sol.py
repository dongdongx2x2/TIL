import sys
sys.stdin = open('15663_input.txt')

input = sys.stdin.readline

def dfs(n, tlst):
    if n == M:
        ans.append(tlst)
        return

    before = 0
    for j in range(N):
        if v[j] == 0 and before != lst[j]:
            before = lst[j]
            v[j] = 1
            dfs(n+1, tlst + [lst[j]])
            v[j] = 0


N, M = map(int, input().split())

lst = sorted(list(map(int, input().split())))

v = [0]*(N+1)
ans = []

dfs(0, [])

for i in ans:
    print(*i)