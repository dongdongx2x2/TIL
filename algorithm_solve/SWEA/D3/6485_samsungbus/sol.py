import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    count = [0] * 5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E + 1):
            count[i] +=1

    P = int(input())
    alist = []
    for _ in range(P):
        p = int(input())
        alist.append(count[p])

    print(f'#{tc}', *alist)
