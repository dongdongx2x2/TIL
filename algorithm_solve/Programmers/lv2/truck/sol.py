# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    
    cur = 0
    
    while truck_weights:
        time += 1
        cur -= bridge.pop(0)
        
        if cur + truck_weights[0] <= weight:
            cur += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    time += bridge_length
    return time