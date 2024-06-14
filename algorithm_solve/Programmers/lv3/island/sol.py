# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x,y):
        x = find(x)
        y = find(y)
        
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
            
    answer = 0
    costs.sort(key = lambda x: x[2])
    
    parent = [i for i in range(n)]
    
    for a, b, cost in costs:
        if find(a) != find(b):
            answer += cost
            union(a,b)
        
                
    return answer