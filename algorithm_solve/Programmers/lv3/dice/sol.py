#https://school.programmers.co.kr/learn/courses/30/lessons/258709

from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    dic = {}
    n = len(dice)
    
    for a_comb in combinations(range(n), n // 2):
        b_comb = [i for i in range(n) if i not in a_comb]
        
        a, b = [], []
        
        for pro in product(range(6), repeat = n//2):
            a.append(sum(dice[i][j] for i, j in zip(a_comb, pro)))
            b.append(sum(dice[i][j] for i, j in zip(b_comb, pro)))
        b.sort()
        
        win = sum(bisect_left(b, num) for num in a)
        dic[win] = list(a_comb)
    
    max_key = max(dic.keys())
                    
    return [x+1 for x in dic[max_key]]