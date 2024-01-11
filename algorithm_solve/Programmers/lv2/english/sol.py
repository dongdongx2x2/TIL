# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    
    k = len(words)
    a, b = 0, 0
    tem = [words[0]]
    for i in range(1, k):
        if tem[-1][-1] != words[i][0] or words[i] in tem:
            a = i % n + 1
            b = i // n + 1
            break
        tem.append(words[i])
        
    answer = [a, b]
    return answer