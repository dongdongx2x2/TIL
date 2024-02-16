# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])
    
    keys = []
    for r in range(1, m + 1):
        for comb in combinations(range(m), r):
            
            tem = []
            for item in relation:
                tuple_tem = []
                for i in comb:
                    tuple_tem.append(item[i])
                tem.append(tuple(tuple_tem))
                
            if len(set(tem)) == n:
                for key in keys:
                    if set(key).issubset(set(comb)):
                        break
                
                else:
                    keys.append(comb)               
        
    print(keys)
    return len(keys)