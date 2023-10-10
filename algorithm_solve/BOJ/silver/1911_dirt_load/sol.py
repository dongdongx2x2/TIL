import sys
sys.stdin = open('1911_input.txt')

input = sys.stdin.readline

N, L = map(int, input().split())

lst = []
for _ in range(N):
    S, E = map(int, input().split())
    lst.append((S, E))
lst.sort()

cur = lst[0][0]
cnt = 0

for s, e in lst:
    if cur > e:
        continue
    elif cur < s:
        cur = s

    dis = e - cur
    r = 1

    if dis % L == 0:
        r = 0
    tem = dis // L + r
    cnt += tem
    cur += tem * L
print(cnt)