import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):

    dump_num = int(input())
    height = list(map(int, input().split()))

    # 덤프횟수 만큼 반복을 돌린다.
    for num in range(dump_num):

        # 일단 건물을 정렬을 시킨다.
          for i in range(len(height)):
                for j in range(len(height)-1):
                    if height[j] > height[j+1]:
                        height[j], height[j+1] = height[j+1], height[j]
          height[-1] -= 1  # 맨뒤 숫자-1 맨앞 항목 +1
          height[0] += 1





    print(f'#{tc} {height[-2]-height[1]}')



