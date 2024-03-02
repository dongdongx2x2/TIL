import sys
sys.stdin = open('9375_input.txt')

input = sys.stdin.readline
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    tem = []
    for j in range(n):
        a, b = input().split()
        tem.append(b)

    Count = Counter(tem)
    cnt = 1
    for key in Count:
        cnt *= Count[key] + 1

    print(cnt-1)