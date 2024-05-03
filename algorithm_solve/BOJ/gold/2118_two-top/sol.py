import sys
sys.stdin = open('2118_input.txt')

input = sys.stdin.readline

n = int(input())
distances = [int(input()) for _ in range(n)]

extended_distances = distances * 2

# 누적합 계산
prefix_sum = [0] * (2 * n + 1)
for i in range(1, 2 * n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + extended_distances[i - 1]

answer = 0
start, end = 0, 1

while start < n:
    # 현재 start와 end 지점 사이의 거리
    current_distance = prefix_sum[end] - prefix_sum[start]

    # 전체 거리의 절반을 넘지 않는 선에서 최대 거리를 찾음
    if current_distance <= prefix_sum[n] / 2:
        answer = max(answer, current_distance)
        end += 1
    else:
        start += 1

print(answer)