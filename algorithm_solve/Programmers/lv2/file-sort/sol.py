# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re
def solution(files):
    tem = []
    for s in files:
        tem.append(re.split(r"([0-9]+)", s))
    
    tem.sort(key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(s) for s in tem]