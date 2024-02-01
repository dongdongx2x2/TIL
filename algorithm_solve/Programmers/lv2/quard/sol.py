# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    
    def check(x, y, n):
        initial = arr[x][y]
        
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != initial:
                    
                    m = n // 2
                    check(x, y, m)
                    check(x, y + m, m)
                    check(x + m, y, m)
                    check(x + m, y + m, m)
                    return
        answer[initial] += 1              
    
    answer = [0, 0]
    check(0, 0, len(arr))
    return answer