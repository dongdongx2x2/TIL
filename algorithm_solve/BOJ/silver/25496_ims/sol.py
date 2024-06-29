import sys
sys.stdin = open('25496_input.txt')

input = sys.stdin.readline

P, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

cnt = 0

for a in range(N):
    if P < 200:
        cnt += 1
        P += A[a]

    else:
        break
print(cnt)