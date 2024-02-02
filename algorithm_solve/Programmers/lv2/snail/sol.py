# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    triangle = [[0] * i for i in range(1, n+1)]
    x, y, number = -1, 0, 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = number
            number += 1
            
    answer = sum(triangle, [])

    return answer