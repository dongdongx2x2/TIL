# https://school.programmers.co.kr/learn/courses/30/lessons/62048?language=python3
import math
def solution(w,h):
    
    return w * h - (w + h - math.gcd(w, h))
