import sys
sys.stdin = open('11051_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())

ans = 1

for i in range(k):
    ans *= n
    n -= 1

tem = 1

for i in range(2, k + 1):
    tem *= i

print((ans // tem) % 10007)