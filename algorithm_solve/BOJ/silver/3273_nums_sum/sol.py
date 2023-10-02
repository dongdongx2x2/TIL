import sys
sys.stdin = open("3273_input.txt")

input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int,input().split())))
x = int(input())

ans = 0
l, r = 0, n-1

while l < r:
    tem = lst[l] + lst[r]
    if tem == x:
        ans += 1
        l += 1
    elif tem < x:
        l += 1
    else:
        r -= 1
print(ans)
