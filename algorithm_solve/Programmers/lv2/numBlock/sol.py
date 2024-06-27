# https://school.programmers.co.kr/learn/courses/30/lessons/12923
def solution(begin, end):
    answer = []
    
    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue
        
        block = 1
        mxmx = int(num**0.5)
        
        for i in range(2, mxmx + 1):
            if num % i == 0:
                if num // i <= 10 ** 7:
                    block = num // i
                    break
                else:
                    block = i
        
        answer.append(block)
    return answer