import sys
sys.stdin = open('1500_input.txt')

input = sys.stdin.readline

S, K = map(int, input().split())

lst = [S // K] * K

for i in range(S % K):
    lst[i] += 1

ans = 1
for i in lst:
    ans *= i
print(ans)


