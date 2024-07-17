import sys
sys.stdin = open('21937_input.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(node):
    global cnt
    v[node] = 1
    cnt += 1

    for next_node in graph[node]:
        if not v[next_node]:
            dfs(next_node)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

x = int(input())

v = [0] * (n+1)
cnt = 0

dfs(x)
print(cnt-1)