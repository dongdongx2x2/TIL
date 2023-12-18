import sys
sys.stdin = open('14395_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, ""))

    v = set()
    v.add(x)

    while q:
        cx, string = q.popleft()
        if cx == y:
            return string

        if cx ** 2 <= y and cx ** 2 not in v:
            q.append((cx**2, string + "*"))
            v.add(cx ** 2)

        if cx * 2 <= y and cx * 2 not in v:
            q.append((cx*2, string + "+"))
            v.add(cx * 2)

        if cx // cx <= y and cx // cx not in v:
            q.append((cx // cx, string + "/"))
            v.add(cx // cx)
    return -1

s, t = map(int, input().split())

if s == t:
    print(0)
    exit()

print(bfs(s, t))