import sys
sys.stdin = open('4803_input.txt')

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = 0
while True:
    T += 1
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    parent = list(range(n+1))
    cycle = set()

    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            cycle.add(parent[a])
            cycle.add(parent[b])

        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])
        union(a,b)

    for i in range(n+1):
        find(i)

    parent = set(parent)
    ans = sum([1 if i not in cycle else 0 for i in parent]) - 1

    if ans == 0:
        print(f"Case {T}: No trees.")
    elif ans == 1:
        print(f"Case {T}: There is one tree.")
    else:
        print(f"Case {T}: A forest of {ans} trees.")