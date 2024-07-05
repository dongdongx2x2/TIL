import sys
sys.stdin = open('13905_input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
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
s, e = map(int, input().split())

parent = [i for i in range(n+1)]

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(reverse=True)

tem = []
for cost, a, b in edges:
    if find(a) != find(b):
        union(a,b)

    if find(s) == find(e):
        tem.append(cost)

if tem:
    print(max(tem))
else:
    print(0)