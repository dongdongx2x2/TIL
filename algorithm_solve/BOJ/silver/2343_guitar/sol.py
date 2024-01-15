import sys
sys.stdin = open('2343_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

s = max(lst)
e = sum(lst)

while s <= e:
    mid= (s + e) // 2

    total = 0
    cnt = 1

    for l in lst:
        if l + total > mid:
            cnt += 1
            total = 0
        total += l

    if cnt <= m:
        ans = mid
        e = mid - 1

    else:
        s = mid + 1
print(ans)

