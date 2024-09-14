# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    
    while True:
        current = queue.pop(0)
        if sum(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer