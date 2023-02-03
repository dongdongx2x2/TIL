import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    D, A, B, F = list(map(int, input().split()))

    # 거리 나누기 (A 속도 더하기 B 속도) 는 시간
    # 시간에 파리가 나는 속도 곱하면댐
    print(f'#{tc} {(D / (A+B))*F}')

