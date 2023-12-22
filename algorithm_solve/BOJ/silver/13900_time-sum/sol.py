import sys
sys.stdin = open('13900_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

sm = sum(lst)

ans = 0

for i in lst:
    sm -= i
    ans += sm * i

print(ans)