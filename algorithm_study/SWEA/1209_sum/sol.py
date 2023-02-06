import sys
sys.stdin = open('input.txt')

for t in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    # 열의 합들    #0,0 0,1 0,2 합, 1,1 1,2 1,3  합 2,1 2,2 2,3합...
    for i in range(100):
        count_a = 0
        for j in range(100):
            count_a += arr[i][j]
        if result < count_a:
            result = count_a

    # 행의 합들    #0,0 1,0 2,0 합, 0,1 1,1 2,1  합 0,2 1,2 2,2합 ....0,100 1,100 2,100 합
    for i in range(100):
        count_b = 0
        for j in range(100):
            count_b += arr[j][i]
        if result < count_b:
            result = count_b

    # 오른 아래 대각선 #00 11 22 33 합
    count_c = 0
    for i in range(100):
        count_c += arr[i][i]
        if result < count_c:
            result = count_c

    # 왼 쪽 아래 대각선 합 #0,99 1,98 2,97 ...
    count_d = 0
    for i in range(100):
        count_d += arr[i][99-i]
        if result < count_d:
            result = count_d

    print(f'#{tc} {result}')