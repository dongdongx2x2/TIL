# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter

def solution(clothes):
    clothes_counter = Counter([kind for name, kind in clothes])
    
    answer = 1
    for count in clothes_counter.values():
        answer *= (count + 1)
    
    return answer - 1