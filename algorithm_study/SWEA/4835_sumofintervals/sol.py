import sys
sys.stdin = open('input.txt')

T = int(input())
# N -
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    ai = list(map(int, input().split()))



    new_list = []
    for i in range(N-M+1): # N - M + 1 개의 case가 나옴
        result = 0
        for j in range(i, i + M):
            result += ai[j]
        new_list.append(result)

    for k in range(N-M+1-1, 0, -1): # 버블정렬
        for q in range(0, k):
            if new_list[q] > new_list[q+1]:
                new_list[q], new_list[q+1] = new_list[q+1], new_list[q]

    print(f'#{tc} {new_list[-1]-new_list[0]}')
