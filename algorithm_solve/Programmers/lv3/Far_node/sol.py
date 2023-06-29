# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def bfs(n,v,arr):
    
    q = deque()
    q.append(n)
    v[n] = 1

    while q:
        cn = q.popleft()
        for j in arr[cn]:
            if v[j] == 0:
                v[j] = v[cn] + 1
                q.append(j)
    
    
def solution(n, edge):                      
    answer = 0
    
    arr = [[] for _ in range(n+1)]
    
    for a, b in edge:
        arr[a].append(b)
        arr[b].append(a)
    # print(arr)
    
    v = [0] * (n+1)
    
    bfs(1,v,arr)
    # print(v)
    
    answer = v.count(max(v))
    
    return answer