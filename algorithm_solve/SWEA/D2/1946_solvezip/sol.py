import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    all = ''
    cnt = 0
    for i in range(N):
        Ci, Ki = input().split()
        Ki = int(Ki)

        word = Ci * Ki
        all += word
        cnt += Ki
    print(f'#{tc}')
    for i in range(cnt//10 + 1): #0.1.2
        print(all[i*10:i*10+10])








