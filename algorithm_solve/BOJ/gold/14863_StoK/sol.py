import sys
sys.stdin = open('14863_input.txt')

input = sys.stdin.readline

N, K = map(int, input().split())
# dp[i][j] = i번째 도시까지 j분을 사용했을 때의 최대 모금액
dp = [[-1] * (K+1) for _ in range(N+1)]
dp[0][0] = 0

# 각 구간별 정보 입력 받기
sections = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    walk_time, walk_money, bike_time, bike_money = sections[i-1]
    for j in range(K+1):
        dp[i][j] = max(dp[i][j], dp[i][j-1])
        # 도보로 이동하는 경우
        if j >= walk_time and dp[i-1][j-walk_time] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-walk_time] + walk_money)
        # 자전거로 이동하는 경우
        if j >= bike_time and dp[i-1][j-bike_time] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-bike_time] + bike_money)

# 출력: N번째 도시까지 K분 이내에 도달했을 때의 최대 모금액
print(max(dp[N]))