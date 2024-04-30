import sys
sys.stdin = open('11657_input.txt')

input = sys.stdin.readline

def bf(start):
    dis[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dis[cur] != INF and dis[next_node] > dis[cur] + cost:
                dis[next_node] = dis[cur] + cost

                if i == n - 1:
                    return True
    return False

INF = int(1e9)
n, m = map(int, input().split())

edges = []
dis = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

if bf(1):
    print("-1")

else:
    for i in range(2, n + 1):
        if dis[i] == INF:
            print("-1")
        else:
            print(dis[i])
