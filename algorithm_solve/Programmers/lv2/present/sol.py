# https://school.programmers.co.kr/learn/courses/30/lessons/258712

from itertools import combinations
from collections import defaultdict

def solution(friends, gifts):
    n = len(friends)
    
    arr = [[0] * n for _ in range(n)]
    
    dic = {}
    for idx, friend in enumerate(friends):
        dic[friend] = idx
    
    for word in gifts:
        give, take = word.split()
        arr[dic[give]][dic[take]] += 1
    
    gift_dict = {}
    
    for friend in friends:
        tem = 0
        for i in range(n):
            tem += arr[i][dic[friend]]
        num = sum(arr[dic[friend]]) - tem
        gift_dict[friend] = num
    
    final_dict = defaultdict(int)
    
    for comb in combinations(friends, 2):
        if arr[dic[comb[0]]][dic[comb[1]]] > arr[dic[comb[1]]][dic[comb[0]]]:
            final_dict[comb[0]] += 1
        
        elif arr[dic[comb[0]]][dic[comb[1]]] < arr[dic[comb[1]]][dic[comb[0]]]:
            final_dict[comb[1]] += 1
        # 같으면
        else:
            if gift_dict[comb[0]] > gift_dict[comb[1]]:
                final_dict[comb[0]] += 1
            elif gift_dict[comb[0]] < gift_dict[comb[1]]:
                final_dict[comb[1]] += 1
    
    if not final_dict:
        return 0
    else:
        return max(final_dict.values())