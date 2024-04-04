# https://school.programmers.co.kr/learn/courses/30/lessons/131130
def solution(cards):
    n = len(cards)
    v = [0] * n
    groups = []
    
    for i in range(n):
        if not v[i]:
            cnt = 0
            while not v[i]:
                v[i] = 1
                i = cards[i] - 1
                cnt += 1
            if cnt > 0:
                groups.append(cnt)
    
    if len(groups) < 2:
        return 0
    
    groups.sort()
    return groups[-1] * groups[-2]
    answer = 0
    return answer