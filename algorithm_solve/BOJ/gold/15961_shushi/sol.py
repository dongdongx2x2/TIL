import sys
sys.stdin = open('15961_input.txt')

input = sys.stdin.readline

from collections import defaultdict

n, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]

dic = defaultdict(int)
dic[c] = 1

mx = 1

lst += lst[:k]

for i in range(k):
    if dic[lst[i]] == 0:
        mx += 1
    dic[lst[i]] += 1

cur = mx

for i in range(k, n+k):
    dic[lst[i-k]] -= 1
    if dic[lst[i-k]] == 0:
        cur -= 1

    dic[lst[i]] += 1
    if dic[lst[i]] == 1:
        cur += 1
    mx = max(mx, cur)
print(mx)