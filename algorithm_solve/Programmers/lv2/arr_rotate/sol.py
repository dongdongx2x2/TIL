# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    arr = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = cnt
            cnt += 1
            
    answer = []
 
    for x1, y1, x2, y2 in queries:
        x1 = x1-1
        y1 = y1-1
        x2 = x2-1
        y2 = y2-1
        tmp = arr[x1][y1]
        mini = tmp
        
        for k in range(x1,x2):
            test = arr[k+1][y1]
            arr[k][y1] = test
            mini = min(mini, test)

        for k in range(y1,y2):
            test = arr[x2][k+1]
            arr[x2][k] = test
            mini = min(mini, test)

        for k in range(x2,x1,-1):
            test = arr[k-1][y2]
            arr[k][y2] = test
            mini = min(mini, test)

        for k in range(y2,y1,-1):
            test = arr[x1][k-1]
            arr[x1][k] = test
            mini = min(mini, test)

        arr[x1][y1+1] = tmp
        answer.append(mini)
                
    return answer