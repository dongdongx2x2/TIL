import sys
sys.stdin = open("2110_input.txt")

input = sys.stdin.readline

N, C = map(int,input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

s = 1
e = lst[-1] - lst[0]
ans = 0

while s <= e:

    mid = (s + e) // 2
    now = lst[0]
    cnt = 1

    for i in range(1, len(lst)):
        if lst[i] >= now + mid:
            now = lst[i]
            cnt += 1

    if cnt >= C:
        ans = mid
        s = mid + 1

    else:
        e = mid - 1
print(ans)
