#https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin,0))
    v = [0] * len(words)
    while q:
        pop_, cnt = q.popleft()
        
        if pop_ == target:
            return cnt
        
        for i in range(len(words)):
            tem_cnt = 0
            if not v[i]:
                for j in range(len(pop_)):
                    if pop_[j] != words[i][j]:
                        tem_cnt += 1
                if tem_cnt == 1:
                    q.append((words[i],cnt + 1))
                    v[i] = 1
    return 0