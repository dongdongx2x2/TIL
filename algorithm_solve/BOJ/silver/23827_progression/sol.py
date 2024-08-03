import sys
sys.stdin = open('23827_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
sm = sum(lst)
ans = 0

for i in lst:
    sm -= i
    ans = (ans + i*sm) % 1000000007

print(ans)
