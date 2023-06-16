#https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
from collections import deque


def solution(n, computers):
    
    
    def bfs(start):
        q = deque()
        q.append(start)
        v[start] = 1
        
        while q:
            now = q.popleft()
            for i in range(n):
                if v[i] == 0 and computers[now][i] == 1:
                    v[i] = 1
                    q.append(i)
    v = [0] * n
    answer = 0
    for i in range(n):
        print(v)
        if v[i] == 0:
            bfs(i)
            print(v)
            answer += 1
    return answer