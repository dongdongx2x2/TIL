# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3

from collections import deque

def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sm1 = sum(q1)
    sm2 = sum(q2)
    
    answer = 0
    
    while q1 and q2:
        if sm1 == sm2:
            return answer           
        
        elif sm1 > sm2:
            sm1 -= q1[0]
            sm2 += q1[0]
            
            tem = q1.popleft()
            q2.append(tem)
        
        elif sm1 < sm2:
            
            sm1 += q2[0]
            sm2 -= q2[0]
            
            tem = q2.popleft()
            q1.append(tem)
        
        answer += 1
        
        if answer == 4*(len(q1)):
            return -1
        
    return -1