# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    tem = []
    answer = 0
    for city in cities:
        city = city.lower()
        if tem and city in tem:
            tem.remove(city)
            tem.append(city)
            answer += 1
        
        else:
            if len(tem) == cacheSize:
                tem.pop(0)
            tem.append(city)
            answer += 5                     

    return answer