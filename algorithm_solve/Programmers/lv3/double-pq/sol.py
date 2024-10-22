# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    min_heap = [] 
    max_heap = []
    
    for operation in operations:
        op, value = operation.split()
        value = int(value)
        
        if op == 'I':
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value) 
        elif op == 'D':
            if not min_heap:
                continue
            
            if value == 1:
                max_value = -heapq.heappop(max_heap)
                min_heap.remove(max_value)
            else:
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
                
    if not min_heap:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]