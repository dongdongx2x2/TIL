# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    answer = 0
    
    dp = [0] * (n+1)
    
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]
    
    answer = dp[n-1] % 1234567
    return answer