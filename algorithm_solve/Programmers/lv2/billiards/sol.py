# https://school.programmers.co.kr/learn/courses/30/lessons/169198

def solution(m, n, startX, startY, balls):
    answer = []
    
    for (a, b) in balls:
        # 각 벽에 맞는 경우의 거리를 계산
        distances = []
        
        # 왼쪽 벽에 맞는 경우
        if not (startY == b and startX > a):
            dist_left = (startX + a) ** 2 + (startY - b) ** 2
            distances.append(dist_left)
        
        # 오른쪽 벽에 맞는 경우
        if not (startY == b and startX < a):
            dist_right = (2 * m - startX - a) ** 2 + (startY - b) ** 2
            distances.append(dist_right)
        
        # 위쪽 벽에 맞는 경우
        if not (startX == a and startY < b):
            dist_top = (startX - a) ** 2 + (2 * n - startY - b) ** 2
            distances.append(dist_top)
        
        # 아래쪽 벽에 맞는 경우
        if not (startX == a and startY > b):
            dist_bottom = (startX - a) ** 2 + (startY + b) ** 2
            distances.append(dist_bottom)
        
        # 최소 거리의 제곱을 결과에 추가
        answer.append(min(distances))
    
    return answer