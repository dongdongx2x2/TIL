import sys
sys.stdin = open('14891_input.txt')

input = sys.stdin.readline

from collections import deque

def right(s, dir):
    if s > 3 or lst[s-1][2] == lst[s][6]:
        return

    if lst[s-1][2] != lst[s][6]:
        right(s + 1, -dir)
        lst[s].rotate(dir)

def left(s, dir):
    if s < 0 or lst[s+1][6] == lst[s][2]:
        return

    if lst[s+1][6] != lst[s][2]:
        left(s-1, -dir)
        lst[s].rotate(dir)

lst = [deque(map(int, input().rstrip())) for _ in range(4)]
# 3번째 오른쪽 7번째 왼쪽

k = int(input())

for _ in range(k):
    n, dir = map(int, input().split())
    n = n - 1

    right(n + 1, -dir)
    left(n - 1, -dir)

    lst[n].rotate(dir)

sm = 0
for i in range(4):
    sm += 2**i * lst[i][0]
    # print(lst[i][0])
print(sm)




