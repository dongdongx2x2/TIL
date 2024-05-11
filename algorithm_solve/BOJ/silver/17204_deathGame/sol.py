import sys
sys.stdin = open('17204_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]

point = 0
m = 0

for i in range(n):
    target = lst[point]
    m += 1
    if target == k:
        print(m)
        break
    point = target
else:
    print(-1)
