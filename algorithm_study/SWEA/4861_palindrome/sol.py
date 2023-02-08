import sys
sys.stdin = open('input.txt')


# 행 우선조회하고 그거 역순 찾기
# 열 우선 조회하고 그거 역순 찾기
# 근데  N과 M이 다른경우도잇기때문에에 M 만큼 빈 리스트 만들어서 돌려야할듯시픔
# 행을 먼저 찾아보자
    #
# 함수로 만들자
def search(N, M, arr):
    lsta = []

    # arr[i:i+M] # N,10 M이 5라하면 0~5, 1~6.. 5~10 i 범위가 0부터 5 까지
    # N 10 M 도10 이면 0~10 i 범위 0부터0
    # N-M인+1듯 i 범위가
    for i in range(N):
        for j in range(N - M + 1):
            lsta.append(arr[i][j:j + M])  # 빈 리스트에 담기
    # print(lsta)
    result = ''
    for i in range(len(lsta)):  #
        if lsta[i] == lsta[i][::-1]:  # 역순인게 잇으면 result 에 값추가
            for j in lsta[i]:
                result += j
    if result: # 리절트값에 값이 잇으면
        return result
    else: #리절트값에 값이 없으면
        # 행과 열을 바꾼다.
        for i in range(N):
            for j in range(N):
                if i < j:
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        return search(N,M,arr)






T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {search(N, M, arr)}')
