# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, deliveries, pickups):
    deliveries = list(reversed(deliveries))
    pickups = list(reversed(pickups))
    a = [1,2]
    
    
    answer = 0
    
    D = 0
    P = 0
    
    for i in range(n):
        D += deliveries[i]
        P += pickups[i]
        
        while D > 0 or P > 0:
            D -= cap
            P -= cap
            answer += (n-i) * 2
    return answer