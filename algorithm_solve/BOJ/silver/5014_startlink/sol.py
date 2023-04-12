import sys
sys.stdin = open('5014_input.txt')

input = sys.stdin.readline
from collections import deque


def bfs(start):

    v = [0] * (F+1)

    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        now = q.popleft()

        if now == G:
            return v[G]-1

        for di in (U, -D):
            ni = now + di
            if 1 <= ni <= F and v[ni] == 0:
                q.append(ni)
                v[ni] = v[now] + 1
    return 'use the stairs'

F, S, G, U, D = map(int,input().split())


print(bfs(S))



