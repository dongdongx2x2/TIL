# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = sum(mid//time for time in times)
        
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer