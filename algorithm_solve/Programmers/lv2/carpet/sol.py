# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    total = brown + yellow
    
    for w in range(3, int(total ** 0.5) + 1):
        if total % w == 0:
            h = total // w
            if (w -2) * (h-2) == yellow:
                return [max(w, h), min(w, h)]