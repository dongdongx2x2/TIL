# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    count = 0 
    zeros = 0

    while s != "1":
        zeros += s.count("0")
        s = bin(len(s.replace("0", "")))[2:]
        count += 1 

    return [count, zeros]