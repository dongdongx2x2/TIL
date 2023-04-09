import sys
sys.stdin = open('17070_input.txt')

input = sys.stdin.readline

# from collections import deque


def check(si, sj, cdir):
    # global cnt

    q = []
    q.append((si,sj, cdir))

    cnt = 0
    while q:
        ci, cj, cdir = q.pop()

        if (ci, cj) == (N-1, N-1):
            cnt += 1

        if cdir == 0: #지금 방향이 가로라면
            for di, dj in ((0, 1), (1, 1)): # 가로와 대각 중하나
                ni, nj = ci+di, cj+dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    if (di, dj) == (1, 1) and arr[ni-1][nj] == 0 and arr[ni][nj-1] == 0:
                        cdir = 2
                        q.append((ni,nj,cdir))
                    elif (di, dj) == (0, 1):
                        cdir = 0
                        q.append((ni, nj, cdir))

        elif cdir == 1: # 방향이 세로라면
            for di, dj in ((1, 0), (1, 1)):
                ni, nj = ci+di, cj+dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    if (di, dj) == (1, 1) and arr[ni-1][nj] == 0 and arr[ni][nj-1] == 0:
                        cdir = 2
                        q.append((ni, nj, cdir))
                    elif (di, dj) == (1, 0):
                        cdir = 1
                        q.append((ni, nj, cdir))

        elif cdir == 2: # 방향 대각이라면
            for di, dj in ((1,0), (0,1), (1,1)):
                ni, nj = ci+di, cj+ dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    if (di, dj) == (0, 1):  # r가로일때는
                        cdir = 0
                        q.append((ni, nj, cdir))
                    elif (di, dj) == (1, 0):
                        cdir = 1
                        q.append((ni, nj, cdir))
                    elif (di, dj) == (1, 1) and arr[ni-1][nj] == 0 and arr[ni][nj-1] == 0:
                        cdir = 2
                        q.append((ni, nj, cdir))
        # print(cdir)
    return cnt

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

# cnt = 0
# bfs 돌면서 시작 점 0,0 끝나느 점 N-1,N-1

# 가로 0, 세로1, 대각 2이라고 표시하자
print(check(0,1,0))
