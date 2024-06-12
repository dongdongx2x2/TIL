import sys
sys.stdin = open('17352_input.txt')

input = sys.stdin.readline

n = int(input())
parents = [i for i in range(n+1)]

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

for _ in range(n-2):
    a, b = map(int, input().split())
    union(a,b)

ans = []

for i in range(1, n+1):
    if i == parents[i]:
        ans.append(i)
print(*ans)
