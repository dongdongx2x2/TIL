# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(N ,road, K):
    dp = [[1e9] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                dp[i][j] = 0
                
    for a,b,c in road:
        if c < dp[a][b]:
            dp[a][b] = c
            dp[b][a] = c
    
    
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])
    
    answer = 0
    for i in range(1, N+1):
        if dp[1][i] <= K:
            answer += 1
    
    return answer