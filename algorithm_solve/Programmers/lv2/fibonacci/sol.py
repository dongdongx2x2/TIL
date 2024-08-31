# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    if n <= 1:
        return n
    
    fib = [0, 1]
    
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % 1234567)
    
    return fib[n]