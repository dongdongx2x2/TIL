import sys
sys.stdin = open('13335_input.txt')

input = sys.stdin.readline

from collections import deque

n, w, L = map(int,input().split())

lst = deque(list(map(int,input().split())))

dis = deque([0] * w)
cnt = 0

while dis:
    cnt += 1
    dis.popleft()

    if lst:
        if sum(dis) + lst[0] > L:
            dis.append(0)
        else:
            dis.append(lst.popleft())
print(cnt)