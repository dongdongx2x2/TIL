import sys
sys.stdin = open('22862_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

s, e, mxmx, odd = 0,0,0,0

while e < n:
    if lst[e] % 2 == 1:
        odd += 1

    while odd > k:
        if lst[s] % 2 == 1:
            odd -= 1
        s += 1

    mxmx = max(mxmx, e - s + 1 - odd)
    e += 1
print(mxmx)