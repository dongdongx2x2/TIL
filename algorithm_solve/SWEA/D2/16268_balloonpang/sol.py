import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    arr = [[0] * (M+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]
    # print(arr) # 0으로 주위를 패킹 해줌


        #좌 상 우 하
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    max = 0
    for x in range(1, N + 1):    # 풍선있는 범위
        for y in range(1, M+1):  #1.1 1.2 1.3...4.1 4.2
            # arr[x + dx[x]][y + dy[y]]
            rlt = 0        # 결과값 항상 0 부터 시작
            rlt += arr[x][y]

            for i in range(4): # 좌상 우하 검색
                rlt += arr[x + dx[i]][y + dy[i]]
                if max <= rlt:
                    max = rlt
    print(f'#{tc} {max}')

