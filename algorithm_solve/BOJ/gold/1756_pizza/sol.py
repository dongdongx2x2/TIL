import sys
sys.stdin = open('1756_input.txt')

input = sys.stdin.readline

d, n = map(int, input().split())

oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(d-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

cur = 0

for i in range(d-1, -1, -1):
    if pizza[cur] > oven[i]:
        continue

    cur += 1

    if cur == n:
        print(i + 1)
        break

if cur != n:
    print(0)
