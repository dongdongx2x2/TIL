import sys
sys.stdin = open('16437_input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(node):
    sheep = 0

    for child in graph[node]:
        sheep += dfs(child)

    if info[node][0] == "W":
        return max(0, sheep - info[node][1])
    else:
        return sheep + info[node][1]

n = int(input())
graph = [[] for _ in range(n+1)]
info = [(0,0)] * (n+1)

for i in range(2, n+1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    graph[p].append(i)
    info[i] = (t, a)

print(dfs(1))
