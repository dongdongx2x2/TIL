# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def is_pal(s):
    if s == s[::-1]:
        return True
    return False

def solution(s):
    n = len(s)
    mxmx = 1
    
    for i in range(n):
        for j in range(i+1, n):
            if is_pal(s[i:j+1]):
                mxmx = max(mxmx, j - i + 1)
    
    return mxmx