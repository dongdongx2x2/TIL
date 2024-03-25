import sys
sys.stdin = open('2230_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

lst = [int(input()) for _ in range(n)]

lst.sort()

s, e = 0, 0
min_diff = 9e9

while s <= e and e < n:
    diff = lst[e] - lst[s]

    if diff < m:
        e += 1

    else:
        min_diff = min(min_diff, diff)
        s += 1
print(min_diff)