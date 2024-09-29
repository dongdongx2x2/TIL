# https://school.programmers.co.kr/learn/courses/30/lessons/12949?language=python3

def solution(arr1, arr2):
    rows_arr1 = len(arr1)
    cols_arr1 = len(arr1[0])
    cols_arr2 = len(arr2[0])
    
    answer = [[0 for _ in range(cols_arr2)] for _ in range(rows_arr1)]
    
    for i in range(rows_arr1):
        for j in range(cols_arr2):
            for k in range(cols_arr1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer