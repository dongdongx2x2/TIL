# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    sm = 0
    for i in range(1,n+1):
        sm = 0
        for j in range(i, n+1):
            sm += j
            if sm == n:
                answer+=1
                break
            elif sm > n:
                break 
    return answer