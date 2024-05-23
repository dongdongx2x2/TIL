# https://school.programmers.co.kr/learn/courses/30/lessons/43164#

from collections import defaultdict

def solution(tickets):
    answer = []
    adj = defaultdict(list)
    
    for a, b in tickets:
        adj[a].append(b)
    
    for a in adj:
        adj[a].sort()
        
    def dfs(start):
        while adj.get(start):
            next = adj[start].pop(0)
            dfs(next)
        answer.append(start)
    
    dfs("ICN")
    return answer[::-1]