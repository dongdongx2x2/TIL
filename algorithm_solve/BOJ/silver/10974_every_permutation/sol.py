import sys
sys.stdin = open('10974_input.txt')

input = sys.stdin.readline


def dfs(n, lst):
    global result

    if n == N:
        result.append(lst)
        return

    for j in range(1, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, lst + [j])
            v[j] = 0


N = int(input())

v = [0] * (N+1)
result = []

dfs(0,[])

for i in result:
    print(*i)