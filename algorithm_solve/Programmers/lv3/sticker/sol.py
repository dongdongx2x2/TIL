# https://school.programmers.co.kr/learn/courses/30/lessons/12971?language=python3

def solution(sticker):
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    dp1 = [0] * (n+1)
    dp1[1] = sticker[0]
    
    for i in range(2, n):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i-1])
        
    dp2 = [0] * (n+1)
    
    for i in range(2, n+1):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i-1])
          

    return max(dp1[n-1], dp2[n])