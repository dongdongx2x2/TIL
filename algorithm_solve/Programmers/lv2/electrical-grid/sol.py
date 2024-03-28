#https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    
    def bfs(start):
        q = deque()
        q.append(start)
        v = [0] * (n + 1)
        v[start] = 1
        
        cnt = 1
        
        while q:
            now = q.popleft()
            for i in graph[now]:
                if not v[i]:
                    q.append(i)
                    v[i] = 1
                    cnt += 1
        return cnt
        
    answer = n
    
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a) - bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer