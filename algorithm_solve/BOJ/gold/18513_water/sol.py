import sys
sys.stdin = open('18513_input.txt')

input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
water = list(map(int, input().split()))

q = deque()
v = set()

for w in water:
    q.append((w, 0))
    v.add(w)

total = 0
house = 0

while q and house < k:
    cur_pos, cur_dis = q.popleft()

    for next_pos in (cur_pos-1, cur_pos+1):
        if next_pos not in v:
            v.add(next_pos)
            total += cur_dis + 1
            house += 1

            q.append((next_pos, cur_dis+1))
            # print(q)
            if house == k:
                break
print(total)
