import sys
sys.stdin = open('13909_input.txt')

input = sys.stdin.readline

n = int(input())

ans = 0
x = 1
while x ** 2 <= n:
    x += 1
    ans += 1
print(ans)