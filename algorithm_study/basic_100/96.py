# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수

arr = [list(map(int, input().split())) for _ in range(19)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    x_idx = x - 1
    y_idx = y - 1

    for i in range(19):
        if arr[x_idx][i] == 1:
            arr[x_idx][i] = 0
        else:
            arr[x_idx][i] = 1

        if arr[i][y_idx] == 1:
            arr[i][y_idx] = 0
        else:
            arr[i][y_idx] = 1

for i in arr:
    print(*i)
