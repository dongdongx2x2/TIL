import sys
sys.stdin = open('13140_input.txt')

input = sys.stdin.readline

from itertools import permutations

n = int(input())

flag = False
for perm in permutations(range(10), 7):
    h, e, l, o, w, r, d = perm

    if h == 0 or w == 0:
        continue

    hello = h * 10000 + e * 1000 + l * 100 + l * 10 + o
    world = w * 10000 + o * 1000 + r * 100 + l * 10 + d

    if hello + world == n:
        print(f"  {hello}")
        print(f"+ {world}")
        print("-------")
        print(str(n).rjust(7))
        flag = True
        break

if not flag:
    print("No Answer")