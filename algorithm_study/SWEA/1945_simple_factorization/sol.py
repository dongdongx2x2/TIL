import sys
sys.stdin = open('input.txt')

T = int(input())
alst = [2, 3, 5, 7, 11]
for tc in range(1, T+1):
    N = int(input())
    # N을 계속 나눈다
    count_l = [0] * len(alst)
    for i in range(len(alst)):
        while N % alst[i] == 0:
            count_l[i] += 1
            N //= alst[i]

    print(f'#{tc}', *count_l)

