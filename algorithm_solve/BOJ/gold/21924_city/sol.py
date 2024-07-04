import sys
sys.stdin = open('21924_input.txt')

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    result += cost

edges.sort()

cnt = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result -= cost
        cnt += 1

if cnt == n - 1:
    print(result)
else:
    print(-1)