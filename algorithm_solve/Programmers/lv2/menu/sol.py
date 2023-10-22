# https://school.programmers.co.kr/learn/courses/30/lessons/72411?language=python3

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for n in course:
        tem = []
        for order in orders:
            com = combinations(sorted(order), n)
            tem += com
        counter = Counter(tem)
        
        if counter and max(counter.values()) >= 2:
            for cnt in counter:
                if counter[cnt] == max(counter.values()):
                    answer.append(''.join(cnt))
    
    return sorted(answer)