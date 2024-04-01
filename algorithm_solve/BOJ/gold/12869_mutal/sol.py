import sys
sys.stdin = open('12869_input.txt')

input = sys.stdin.readline

from collections import deque
from itertools import permutations

n = int(input())
scv = list(map(int, input().split())) + [0] * (3-n)

v = [[[0] * 61 for _ in range(61)] for _ in range(61)]

v[scv[0]][scv[1]][scv[2]] = 1

q = deque()
q.append((scv[0], scv[1], scv[2], 0))

attacks = list(permutations([9,3,1]))

while q:
    scv1, scv2, scv3, cnt = q.popleft()

    if scv1 == 0 and scv2 == 0 and scv3 == 0:
        print(cnt)
        break

    for attack in attacks:
        cscv1, cscv2, cscv3 = max(0, scv1-attack[0]), max(0, scv2-attack[1]), max(0, scv3-attack[2])
        if not v[cscv1][cscv2][cscv3]:
            v[cscv1][cscv2][cscv3] = 1
            q.append((cscv1, cscv2, cscv3, cnt + 1))