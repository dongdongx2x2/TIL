import sys
sys.stdin = open('15652_input.txt')

input = sys.stdin.readline


def dfs(n,lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(1, N+1):
        if (not lst) or lst[-1] <= j:
            dfs(n+1, lst + [j])


N, M = map(int, input().split())


ans = []

dfs(0, [])

for lst in ans:
    print(*lst)