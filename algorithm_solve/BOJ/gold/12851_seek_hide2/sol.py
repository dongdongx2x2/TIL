import sys
sys.stdin = open('12851_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(N):
    q = deque()
    q.append(N)

    v[N] = 1
    global cnt
    while q:
        cN = q.popleft()
        if cN == K:
            cnt += 1
        for nN in (cN-1, cN+1, cN*2):
            if 0 <= nN < 100001:
                if v[nN] == 0 or v[nN] == v[cN] + 1:
                    v[nN] = v[cN] + 1
                    q.append(nN)

N, K = map(int, input().split())

v = [0] * 100001
cnt = 0
bfs(N)
print(v[K]-1)
print(cnt)
