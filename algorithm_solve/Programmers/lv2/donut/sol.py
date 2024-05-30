# https://school.programmers.co.kr/learn/courses/30/lessons/258711

from collections import defaultdict

def solution(edges):
    dic = defaultdict(lambda: [0,0])
    
    for a, b in edges:
        dic[a][0] += 1
        dic[b][1] += 1
        
    answer = [0,0,0,0]
    
    for node, item in dic.items():
        give = item[0]
        take = item[1]
        
        if give >= 2 and take == 0:
            answer[0] = node
        elif give >= 2 and take >=2:
            answer[3] += 1
        elif give == 0 and take >= 1:
            answer[2] += 1
    tem = dic[answer[0]][0]
    answer[1] = tem - answer[2] - answer[3]
    return answer