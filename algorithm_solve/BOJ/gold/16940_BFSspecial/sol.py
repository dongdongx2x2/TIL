import sys
sys.stdin = open('16940_input.txt')

input = sys.stdin.readline

from collections import deque

def check_bfs():
    if target[0] != 1:
        return 0

    v = [0] * (n+1)
    q = deque()
    q.append(1)
    v[1] = 1

    idx = 1

    while q:
        cur = q.popleft()

        children = []
        for next_node in adj[cur]:
            if not v[next_node]:
                v[next_node] = 1
                children.append(next_node)

        children_set = set(children)
        expected_set = set(target[idx:idx + len(children)])

        if children_set != expected_set:
            return 0

        q.extend(target[idx:idx + len(children)])

        idx += len(children)
    return 1

n = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
target = list(map(int, input().split()))

print(check_bfs())