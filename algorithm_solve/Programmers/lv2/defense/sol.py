# https://school.programmers.co.kr/learn/courses/30/lessons/142085
import heapq

def solution(n, k, enemy):
    answer, sum_enemy = 0, 0
    hq = []
    
    for e in enemy:
        heapq.heappush(hq, -e)
        sum_enemy += e
        if sum_enemy > n:
            if k == 0:
                break
            sum_enemy += heapq.heappop(hq)
            k -= 1
        answer += 1
    return answer