# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    graph = [[0]*(n+1) for _ in range(n+1)]
    
    for winner, loser in results:
        graph[winner][loser] = 1
        graph[loser][winner] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    
    answer = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if i == j:
                count += 1
            elif graph[i][j] != 0:
                count += 1

        if count == n:
            answer += 1
    
    return answer