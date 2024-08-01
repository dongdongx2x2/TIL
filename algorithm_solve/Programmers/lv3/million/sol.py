# https://school.programmers.co.kr/learn/courses/30/lessons/138475
def solution(e, starts):
    count = [0] * (e + 1)
    for i in range(1, int(e**0.5) + 1):
        for j in range(i*i, e + 1, i):
            count[j] += 2
        count[i*i] -= 1
    
    max_count = [0] * (e + 1)
    max_num = e
    for i in range(e, min(starts) - 1, -1):
        if count[i] >= count[max_num]:
            max_num = i
        max_count[i] = max_num
    
    return [max_count[s] for s in starts]