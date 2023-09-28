import sys
sys.stdin = open('2012_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(int(input()) for _ in range(N))

lst.sort()

ans = 0
for i in range(1, N+1):
    ans += abs(i-lst[i-1])
print(ans)