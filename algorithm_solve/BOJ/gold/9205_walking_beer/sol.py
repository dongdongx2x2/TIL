import sys
sys.stdin = open('9205_input.txt')

input = sys.stdin.readline
from collections import deque


def bfs(x, y):

    v = [0] * n

    q = deque()
    q.append((x,y))

    while q:
        cx, cy = q.popleft()
        if abs(cx-goalX) + abs(cy-goalY) <= 1000:
            return 'happy'

        for i in range(n):
            if v[i] == 0:
                nx, ny = conv[i]
                if abs(nx-cx) + abs(ny-cy) <= 1000:
                    q.append((nx,ny))
                    v[i] = 1
    return 'sad'


t = int(input())

for _ in range(t):
    n = int(input())

    # 50미터당 한병 마셔야함 한박스에 20병 한박스당 1000미터 갈수있음 편의점 갈떄마다 충전1000미터터
    homeX, homeY = map(int,input().split())

    conv = []
    for _ in range(n):
        x, y = map(int,input().split())
        conv.append((x,y))

    goalX, goalY = map(int, input().split())

    print(bfs(homeX,homeY))


