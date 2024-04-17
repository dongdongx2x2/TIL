import sys
sys.stdin = open('13144_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

s, e, ans = 0,0,0

check = [0] * 100001

while s < n and e < n:
    if check[lst[e]] == 0:
        check[lst[e]] = 1
        ans += (e - s + 1)
        e += 1

    else:
        check[lst[s]] = 0
        s += 1

print(ans)