import sys
sys.stdin = open('20303_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(start):
    friend_cnt = 1

    candy_cnt = candy[start]
    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        now = q.popleft()
        for next in friend[now]:
            if v[next] == 0:
                q.append(next)
                v[next] = 1
                friend_cnt += 1
                candy_cnt += candy[next]

    return [friend_cnt, candy_cnt]

n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
friend = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

child_group = []
v = [0] * (n+1)
for i in range(1, n + 1):
    if v[i] == 0:
        child_group.append(bfs(i))

dp = [0] * (k+1)

for i in range(len(child_group)):
    friend_cnt, candy_cnt = child_group[i]

    for j in range(k, friend_cnt-1, -1):
        dp[j] = max(dp[j], dp[j-friend_cnt] + candy_cnt)

print(dp[k-1])