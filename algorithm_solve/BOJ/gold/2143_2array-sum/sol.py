import sys
sys.stdin = open('2143_input.txt')

input = sys.stdin.readline

from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_dic = defaultdict(int)

for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += a[j]
        a_dic[sm] += 1

ans = 0

for i in range(m):
    sm = 0
    for j in range(i, m):
        sm += b[j]
        ans += a_dic[t - sm]

print(ans)