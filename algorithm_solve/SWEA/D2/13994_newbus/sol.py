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
    # print(arr)

    max_arr= []
    for i in range(len(arr)):
        max_arr.append(arr[i][1])
        max_arr.append(arr[i][2])
    # print(max(max_arr))

    count_arr = [0]  * (max(max_arr)+1)
    # print(count_arr)

    for j in range(len(arr)):
        # print(arr[j][0])
        if arr[j][0] == 1:     # 일반 버스라면
            for k in range(arr[j][1], arr[j][2]+1): #arr 의 idx [1]부터 [2]값까지 다 1 추가
                count_arr[k] += 1
    # print(count_arr)
        elif arr[j][0] == 2: # 급행 버스라면
            if arr[j][1] % 2 == 1: #급행버스 A가 홀수라면
                count_arr[arr[j][1]] += 1 # 양 끝 1 추가
                count_arr[arr[j][2]] += 1
                for l in range(arr[j][1]+1, arr[j][2]): # 사이에
                    if l % 2 == 1:          # 홀수들
                        count_arr[l] += 1 # 1추가
            else: # 급행버스 A가 짝수라면
                count_arr[arr[j][1]] += 1 # 양 끝 1 추가
                count_arr[arr[j][2]] += 1
                for m in range(arr[j][1]+1, arr[j][2]): # 사이에 짝수
                    if m % 2 == 0:
                        count_arr[m] += 1
        else: # 광역 급행 버스라면
            if arr[j][1] % 2 == 1: # 광역버스 A가 홀 수라면
                count_arr[arr[j][1]] += 1 # 양 끝 1 추가
                count_arr[arr[j][2]] += 1
                for n in range(arr[j][1]+1, arr[j][2]): # 사이에 3배수이면서 10배수 아닌거 추가
                    if n % 3 == 0 and n % 10 != 0:
                        count_arr[n] += 1
            else: # 광역 버스A가 짝수라면
                count_arr[arr[j][1]] += 1 # 양 끝 1 추가
                count_arr[arr[j][2]] += 1
                for o in range(arr[j][1]+1, arr[j][2]): # 사이에 4 배수 1추가
                    if o % 4 == 0:
                        count_arr[o] +=1

    # print(max(count_arr))
    print(f'#{tc} {max(count_arr)}')

