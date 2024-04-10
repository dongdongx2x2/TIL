import sys
sys.stdin = open('10775_input.txt')

input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[x] = y

g = int(input())
p = int(input())

planes = [int(input()) for _ in range(p)]

parent = [i for i in range(g+1)]

cnt = 0

for plane in planes:
    next_gate = find(plane)
    if next_gate == 0:
        break

    union(next_gate, next_gate-1)

    cnt += 1
print(cnt)