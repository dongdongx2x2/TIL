import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int,input().split()))

    result = 0
    # 양 끝 두자리 뺴기기
    for i in range(2, N-2):
       tmp = arr[i]  # 현재 조사하는 높이 #최대 조망권
       # 현재 위치 기준 좌우 2칸씩 조사해야함
       for j in range(i-2, i+3):
           # 같은 건물을 비교 x
           if i == j:
               continue
           # 조사 하는 대상이 양 옆 두개씩 건물보다크고,
           # 각 차이가 조망권보다 작으면
           if arr[i] > arr[j] and tmp > arr[i] - arr[j]:
               tmp = arr[i] - arr[j] # 변경
            #양 옆보다 작거나 같은 경우
           # 조사 x
           elif arr[i] <= arr[j]:
               break
       else:
           result += tmp

    print(f'#{tc} {result}')