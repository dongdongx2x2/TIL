#https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    words = s.lower().split(' ')
    
    jaden_cased = [word.capitalize() for word in words]
    
    return ' '.join(jaden_cased)