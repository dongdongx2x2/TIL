import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    # 각각 숫자 리스트 형태로받기
    # 젤 높은 숫자 만큼 [0] * 최댓값
    # 각ㄱ 각 마다 카운트 +1 해주기

    N = int(input())

    arr = []
    for _ in range(1, N+1):
        arr.append(list(map(int, input().split())))
    print(arr)

    max_arr= []
    for i in range(len(arr)):
        max_arr.append(arr[i][1])
        max_arr.append(arr[i][2])
    print(max(max_arr))

    count_arr = [0]  * max(max_arr)
    print(count_arr)

    for j in range(len(arr)):
        print(arr[j][0])
        if arr[j][0] == 1:     # 일반 열차면
            for k in range(arr[j][1], arr[j][2]+1): #arr 의 idx [1]부터 [2]값까지 다 1 추가
                count_arr[k] += 1
    # print(count_arr)
        elif arr[j][0] == 2: # 급행 버스 라면
            if arr[j][1] % 2 == 0: #A가 짝수라면
                for q in range(arr[j][1], arr[j][2]+1):
                    if q % 2 == 0: # 짝수 인덱스에
                        count_arr[q] +=1 # 1 추가
            else: # A가 홀수라면
                for t in range(arr[j][1], arr[j][2]+1):
                    if t % 2 == 1:
                        count_arr[t] += 1
    print(count_arr)



