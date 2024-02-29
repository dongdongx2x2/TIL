# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations

def solution(expression):
    answer = []
    operator = ['-', '+', '*']
    
    for per in permutations(operator,3):
        a = per[0]
        b = per[1]
        tem_lst = []
        
        for i in expression.split(a):
            tem = [f"({j})" for j in i.split(b)]
            tem_lst.append(f"({b.join(tem)})")
        
        answer.append(abs(eval(a.join(tem_lst))))
    
    return max(answer)