import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    # print(matrix)
    N = int(input())

    for _ in range(N): # input값 할당
        r1, c1, r2, c2, color = map(int, input().split())
        # print(r1,c1,r2,c2,color)
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 1 : # 빨강일때
                    matrix[i][j] += 1
                elif color == 2: # 파랑일 떄
                    matrix[i][j] += 2
    count = 0
    for i in range(10):
        for j in range(10):
           if matrix[i][j] == 3:
               count += 1
    print(f'#{tc} {count}')






        