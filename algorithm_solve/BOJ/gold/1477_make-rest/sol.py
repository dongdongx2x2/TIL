import sys
sys.stdin = open('1477_input.txt')

input = sys.stdin.readline

n, m, l = map(int, input().split())
lst = list(map(int, input().split()))

lst.append(0)
lst.append(l)
lst.sort()

s, e = 1, l-1
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0

    for i in range(1, len(lst)):
        if lst[i] - lst[i-1] > mid:
            cnt += (lst[i] - lst[i-1] -1) // mid

    if cnt > m:
        s = mid + 1

    else:
        e = mid - 1
        ans = mid

print(ans)