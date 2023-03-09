import sys
sys.stdin = open('13549_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(N):

    q = deque()
    q.append(N)

    v[N] = 1

    while q:
        cN = q.popleft()

        if cN == K:
            return v[cN]

        for nN in (cN-1, cN+1, cN*2):
            if 0 <= nN< 100001 and v[nN] == 0:
                if nN == cN*2:
                    v[nN] = v[cN]
                    q.insert(0,nN)
                else:
                    v[nN] = v[cN] + 1
                    q.append(nN)

N, K = map(int, input().split())

v = [0] * 100001
print(bfs(N)-1)