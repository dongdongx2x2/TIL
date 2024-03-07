#https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    
    v = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for p, c in edges:
            if v[p] and not v[c]:
                v[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                v[c] = 0
    
    v[0] = 1
    dfs(1,0)

    return max(answer)