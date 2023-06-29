# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    n = len(citations)
    
    citations.sort()
     
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0