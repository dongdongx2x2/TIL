# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    freq = list(c.values())
    freq.sort(reverse=True)
    
    cnt = 0
    for fre in freq:
        k -= fre
        answer += 1
        
        if k <= 0:
            break
    return answer