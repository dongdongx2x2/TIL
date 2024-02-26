import sys
sys.stdin = open('1865_input.txt')

input = sys.stdin.readline

def bf(start):
    dis[start] = 0

    for i in range(n):
        for j in range(1, n+1):
            for next, cost in graph[j]:
                if dis[next] > dis[j] + cost:
                    dis[next] = dis[j] + cost
                    if i == n-1:
                        return True
    return False

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    dis = [1e9] * (n+1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    if bf(1):
        print("YES")
    else:
        print("NO")
