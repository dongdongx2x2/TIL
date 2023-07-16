# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):
    n, m = len(users), len(emoticons)

    discount = [(10,9), (20, 8), (30, 7), (40, 6)]
    answer = [0, 0]
    
    for disc in product(discount, repeat = m):
        
        tem = [0, 0]
        
        for a, b in users:
            sm = 0
            
            for i in range(m):
                if a <= disc[i][0]:
                    sm += emoticons[i]//10*disc[i][1]
            
            if b <= sm:
                tem[0] += 1
            elif b > sm:
                tem[1] += sm
        
        if answer[0] > tem[0]:
            continue
        elif answer[0] < tem[0]:
            answer = tem
        elif answer[0] == tem[0]:
            if answer[1] >= tem[1]:
                continue
            elif answer[1] < tem[1]:
                answer = tem
    return answer