import sys

sys.stdin = open('14226_input.txt')

input = sys.stdin.readline

from collections import deque


def bfs(n, clip):
    q = deque()
    q.append((n, clip))

    v = dict()
    v[(1,0)] = 0

    while q:
        cn, c_clip = q.popleft()

        if cn == S:
            return v[(cn, c_clip)]

        if (cn, cn) not in v.keys():
            v[(cn,cn)] = v[(cn, c_clip)] + 1
            q.append((cn,cn))

        if (cn + c_clip, c_clip) not in v.keys():
            v[(cn + c_clip, c_clip)] = v[(cn, c_clip)] + 1
            q.append((cn + c_clip, c_clip))

        if (cn - 1, clip) not in v.keys():
            v[(cn-1, c_clip)] = v[(cn, c_clip)] + 1
            q.append((cn - 1, c_clip))


S = int(input())

print(bfs(1, 0))

