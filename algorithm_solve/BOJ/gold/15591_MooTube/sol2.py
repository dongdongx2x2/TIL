import sys
sys.stdin = open('15591_input.txt')

input = sys.stdin.readline

from collections import deque, defaultdict

def bfs(k,v):
    q = deque()
    q.append((v, 1000000001))

    vis = [0] * (N + 1)
    vis[v] = 1

    cnt = 0

    while q:
        v, usado = q.popleft()

        for n_v, n_usado in arr[v]:
            n_usado = min(usado, n_usado)

            if n_usado >= k and vis[n_v] == 0:
                cnt += 1
                q.append((n_v, n_usado))
                vis[n_v] = 1
    return cnt

N, Q = map(int,input().split())

arr = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int,input().split())
    arr[p].append((q,r))
    arr[q].append((p,r))
for _ in range(Q):
    k, v = map(int,input().split())

    print(bfs(k,v))



