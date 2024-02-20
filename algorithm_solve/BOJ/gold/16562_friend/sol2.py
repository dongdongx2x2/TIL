import sys
sys.stdin = open('16562_input.txt')

input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if cost[x] > cost[y]:
        cost[x] = 0
        parent[x] = y
    else:
        cost[y] = 0
        parent[y] = x


n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = list(range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

money = sum(cost)
if money <= k:
    print(money)
else:
    print("Oh no")