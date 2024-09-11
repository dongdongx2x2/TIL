# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:  # 짝수인 경우
            n = n // 2  # 순간이동
        else:  # 홀수인 경우
            n -= 1  # 1칸 점프
            ans += 1
    
    return ans