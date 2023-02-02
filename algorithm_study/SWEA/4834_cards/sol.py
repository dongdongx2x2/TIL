import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input()))

    count_list = [0] * 10 #카운트 리스트만들기 숫자 각 몇갠지 알기위해
    for i in range(N):
        count_list[arr[i]] += 1


    max = count_list[9] # 제일 높은 숫자 max로 놔두고
    for j in range(len(count_list)-1): # 제일 높은 값 찾기
        if count_list[j] <= count_list[j+1] and max <= count_list[j+1]:
            max = count_list[j+1]
    # print(max)

    for t in range(9, -1, -1):  # 뒤에서 부터 검사 - 같으면 높은 숫자 나오게 하기위함
        if count_list[t] == max:
            # print(t)
            break
    print(f'#{tc} {t} {max}')
