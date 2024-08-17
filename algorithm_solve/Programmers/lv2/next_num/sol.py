# https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    cnt_ones = bin(n).count('1')
    
    next_num = n + 1
    while True:
        if bin(next_num).count('1') == cnt_ones:
            return next_num
        next_num += 1