# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        
        tem = (first + (second) * 2)
        heapq.heappush(scoville, tem)
        answer += 1
        
    return answer