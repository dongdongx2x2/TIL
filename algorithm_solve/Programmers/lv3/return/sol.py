# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque

def solution(n, roads, sources, destination):
    
    def bfs(start):
        q = deque()
        q.append(start)
        
        v = [-1] * (n+1)
        v[start] = 0
        
        while q:
            cur = q.popleft()

            for next_node in graph[cur]:
                if v[next_node] == -1:
                    v[next_node] = v[cur] + 1
                    q.append(next_node)

        return v
    
    graph = [[] for _ in range(n+1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = bfs(destination)
    
    answer = [dist[source] for source in sources]  
    
    return answer