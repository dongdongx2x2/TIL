# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    
    for word in skill_trees:
        tem = ''
        for c in word:
            if c in skill:
                tem += c
        if skill[:len(tem)] == tem:
            answer += 1      
         
    return answer