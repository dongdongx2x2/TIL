import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = [[0 for _ in range(N)] for _ in range(N)]

    # arr 에 1~ N 까지의 숫자를 달팽이 모양으로 넣어야한다..,
    # 어떻게 넣을까
    # 델타 검색을 사용해보자

    #    우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    count = 1 #첫시작 1
    dir = 0  #방향을 나타넴
    x, y = 0, 0 # 시작 좌표표
    arr[x][y] = count # 시작 값

    while count < N**2:
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 범위 설정
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            count += 1 #숫자 증가
            arr[nx][ny] = count
            x, y = nx, ny # 위치 이동
        else:
            dir += 1    # 방향전환
            if dir >=4: # 방향 4종류
                dir = 0 # 한바퀴다돌면 초기화
    print(f'#{tc}')
    for i in arr:
        print(*i)

