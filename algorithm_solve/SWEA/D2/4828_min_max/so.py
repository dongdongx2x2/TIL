import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if ai[j] > ai[j+1]:
                ai[j], ai[j+1] = ai[j+1], ai[j]
    print(f'#{tc} {ai[-1]-ai[0]}')

