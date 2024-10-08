# https://school.programmers.co.kr/learn/courses/30/lessons/84512#
from itertools import product

def solution(word):
    answer = []
    vowels = ["A", "E", "I", "O", "U"]
    
    for i in range(1, 6):
        for pro in product(vowels, repeat = i):
            answer.append(''.join(pro))
    answer.sort()
    
    return answer.index(word) + 1