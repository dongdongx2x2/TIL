import sys
sys.stdin = open('input.txt')

for tc in (range(1, 11)):
    T= int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 100x100 2차원 배열 만들기

    for i in range(100):
        if arr[99][i] == 2: # 2가 들어을떄의 인덱스 값
            two_x, two_y = 99, i

    # 상, 좌, 우
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    while two_x != 0:
        for i in range(3): # 3 방향 조사하기
            nx = two_x + dx[i]
            ny = two_y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1: # 범위가0~99고 다음 갈려고하는 칸의 숫자가 1이면
                two_x = nx
                two_y = ny
                arr[two_x][two_y] = 0
    print(f'#{tc} {two_y}')



