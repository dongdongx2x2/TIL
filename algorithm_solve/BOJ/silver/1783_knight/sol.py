import sys
sys.stdin = open('1783_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m - 1) // 2 + 1))
elif m <= 6:
    print(min(4, m))
else:
    print(m - 2)
