# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer = 0
    N = len(routes)
    routes.sort(key=lambda x:x[1])
    
    last = routes[0][1]
    
    for i in range(1, N):
        if last < routes[i][0]:
            answer += 1
            last = routes[i][1]
            
    return answer+1