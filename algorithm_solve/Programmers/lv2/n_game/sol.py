# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def solution(n, t, m, p):
    
    def ginbup(number, n):
        if number == 0:
            return '0'
        NUMBERS = "0123456789ABCDEF"
        res = ''
        while number > 0:
            number, mod = divmod(number,n)
            res += NUMBERS[mod]
        return res[::-1]
        
    answer = ''
    candidate = []
    
    for i in range(t*m):
        conv = ginbup(i, n)
        for c in conv:
            candidate.append(c)
    for i in range(p-1, t*m, m):
        answer += candidate[i]
        
    return answer