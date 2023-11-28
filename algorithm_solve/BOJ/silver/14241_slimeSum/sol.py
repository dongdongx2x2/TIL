import sys
sys.stdin = open('14241_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans = 0
sm = 0

for i in range(0, N - 1):
    ans = lst[i] * lst[i + 1]
    lst[i + 1] = lst[i] + lst[i + 1]
    sm = sm + ans
print(sm)
