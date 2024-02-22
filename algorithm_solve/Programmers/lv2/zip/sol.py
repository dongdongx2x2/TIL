# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1
    
    answer = []
    w, c = 0, 0
    
    while True:
        c += 1
        if msg[w:c+1] not in dic:
            answer.append(dic[msg[w:c]])
            dic[msg[w:c+1]] = len(dic) + 1
            w = c
        if c == len(msg):
            break
    answer.append(dic[msg[w:]])
             
    return answer