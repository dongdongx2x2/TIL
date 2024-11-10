import sys
sys.stdin = open('20300_input.txt')

input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

t.sort()

m = 0
if n % 2 == 0:
    for i in range(n // 2):
        m = max(m, t[i] + t[n-1-i])
else:
    m = t[-1]
    for i in range(n // 2):
        m = max(m, t[i] + t[n-2-i])

print(m)