import sys
sys.stdin = open('13913_input.txt')

input = sys.stdin.readline
from collections import deque

def path(cur):
    data = []

    tem = cur
    for _ in range(v[cur] + 1):
        data.append(tem)
        tem = move[tem]
    print(*data[::-1])

def bfs(start):
    q = deque()
    q.append(start)

    v[start] = 0

    while q:
        cur = q.popleft()
        if cur == k:
            print(v[cur])
            path(cur)
            return

        for next_node in (cur-1, cur+1, cur * 2):
            if 0<=next_node <= 100000 and v[next_node] == -1:
                v[next_node] = v[cur] + 1
                q.append(next_node)
                move[next_node] = cur

n, k = map(int, input().split())
move = [0] * 100001
v = [-1] * 100001
bfs(n)