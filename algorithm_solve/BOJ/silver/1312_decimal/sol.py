import sys
sys.stdin = open('1312_input.txt')

input = sys.stdin.readline

A, B, N = map(int, input().split())

for i in range(N):
    A = (A % B) * 10
    ans = A // B
print(ans)
