import sys
sys.stdin = open('4195_input.txt')

input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

t = int(input())

for _ in range(t):
    parent = dict()
    number = dict()

    f = int(input())
    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x,y)
        print(number[find(x)])

