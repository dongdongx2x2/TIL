import sys
sys.stdin = open('2644_input.txt')

input = sys.stdin.readline

def bfs(s):
    q = [s]
    v = [0] * (N + 1)
    v[s] = 1
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    if v[y] == 0:
        return -1

    else:
        return v[y]-1

N = int(input())

x, y = map(int, input().split())

e = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(e):
    p, c = map(int,input().split())
    adj[c].append(p)
    adj[p].append(c)
# print(adj) # 부모 자식 관계 인접행렬

print(bfs(x))
