import sys

sys.stdin = open("1246_input.txt")

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(m)]
lst.sort()
res = 0
target = 0
for i in range(m):
    egg = min(m - i, n)
    if res < lst[i] * egg:
        res = lst[i] * egg
        target = lst[i]

print(target, res)
