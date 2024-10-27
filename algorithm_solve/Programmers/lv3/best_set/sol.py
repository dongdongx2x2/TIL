# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if s < n:
        return [-1]
    
    base = s // n

    result = [base] * n
    
    remainder = s % n
    for i in range(remainder):
        result[-(i+1)] += 1
    
    return result