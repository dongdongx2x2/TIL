import sys
sys.stdin = open('20040_input.txt')

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(1, m + 1):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(i)
        break
    else:
        union(a, b)
else:
    print(0)