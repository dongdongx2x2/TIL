# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3

def solution(phone_book):
    dic = dict()
    
    for phone in phone_book:
        dic[phone] = 1
    
    for phone in phone_book:
        tem = ""
        for num in phone:
            tem += num
            if tem in dic and tem != phone:
                return False
    return True