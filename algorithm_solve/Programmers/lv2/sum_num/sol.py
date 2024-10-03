# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    n = len(elements)
    
    extended_elements = elements * 2
    
    sums = set()
    
    for start in range(n):
        for length in range(1, n + 1):
            sums.add(sum(extended_elements[start:start+length]))
    
    return len(sums)