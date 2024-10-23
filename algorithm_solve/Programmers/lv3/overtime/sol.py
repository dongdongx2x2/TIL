# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        max_work = heapq.heappop(works)
        heapq.heappush(works, max_work + 1)
 
    return sum(w**2 for w in works)