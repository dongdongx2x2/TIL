# https://school.programmers.co.kr/learn/courses/30/lessons/64064
from itertools import permutations

def isMatch(per_set, banned_set):
    for i in range(len(per_set)):
        if len(per_set[i]) != len(banned_set[i]):
            return False
        for j in range(len(per_set[i])):
            if banned_set[i][j] == "*":
                continue
            if per_set[i][j] != banned_set[i][j]:
                return False
    return True
    
def solution(user_id, banned_id):
    answer = []
    
    for per_set in permutations(user_id, len(banned_id)):
        if isMatch(per_set, banned_id):
            per_set = set(per_set)
            if per_set not in answer:
                answer.append(per_set)
    return len(answer)