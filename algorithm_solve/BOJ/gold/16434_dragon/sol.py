import sys
sys.stdin = open('16434_input.txt')

input = sys.stdin.readline

import math

def is_possible(hp):
    cur_hp = hp
    cur_atk = hatk

    for t, a, h in rooms:
        if t == 1:
            atk_cnt = math.ceil(h/cur_atk)
            damage = (atk_cnt - 1) * a
            cur_hp -= damage
            if cur_hp <= 0:
                return False

        else:
            cur_atk += a
            cur_hp = min(hp, cur_hp + h)

    return True

n, hatk = map(int, input().split())

rooms = [list(map(int, input().split())) for _ in range(n)]

left, right = 1, n * int(10e6) * int(10e6)
ans = right

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
