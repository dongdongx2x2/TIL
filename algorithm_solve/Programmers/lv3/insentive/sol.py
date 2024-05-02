# https://school.programmers.co.kr/learn/courses/30/lessons/152995#
def solution(scores):
    answer = 1
    w_a, w_b = scores[0]
    WanHo = w_a + w_b
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    mxmx = 0
    
    for a, b in scores:
        if w_a < a and w_b < b:
            return -1
        
        if b >= mxmx:
            mxmx = b
            if a + b > WanHo:
                answer += 1
    return answer