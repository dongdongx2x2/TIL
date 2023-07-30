#https://school.programmers.co.kr/learn/courses/30/lessons/92342
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    mx_gap = 0
    score = list(range(11))
    
    for combi in list(combinations_with_replacement(score, n)):
        lion = 0
        appeach = 0
        
        tem = [0 for _ in range(11)]
        for score_char in combi:
            tem[10 - score_char] += 1
        
        for i in range(11):
            if tem[i] == info[i] == 0:
                continue
            if tem[i] > info[i]:
                lion += (10-i)
            else:
                appeach += (10-i)
        
        gap = lion - appeach
        if lion > appeach and mx_gap < gap:
            mx_gap = gap
            answer = tem          
            
    return answer