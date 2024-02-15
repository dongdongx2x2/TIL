# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = {}
    his = []
    
    for rec in record:
        info = rec.split()
        if info[0] in ["Enter", "Change"]:
            dic[info[1]] = info[2]
            
    for rec in record:
        info = rec.split()
        if info[0] == "Enter":
            answer.append(f"{dic[info[1]]}님이 들어왔습니다.")
        elif info[0] == "Leave":
            answer.append(f"{dic[info[1]]}님이 나갔습니다.")           
    return answer