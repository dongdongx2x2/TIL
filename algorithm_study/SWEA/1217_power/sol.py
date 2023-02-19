import sys
sys.stdin = open('input.txt')

def power(N, M):

    if M == 1:
        return N
    else:
        return power(N, M-1)*N

for _ in range(1, 11):
    tc = int(input())

    N, M = map(int, input().split())

    print(f'#{tc} {power(N, M)}')
