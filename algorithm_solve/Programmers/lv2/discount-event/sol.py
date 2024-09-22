# https://school.programmers.co.kr/learn/courses/30/lessons/131127?language=python3

from collections import Counter


def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want, number))
    want_counter = Counter(want_dict)

    for i in range(len(discount) - 9):
        discount_counter = Counter(discount[i:i + 10])
        if want_counter == discount_counter:
            answer += 1

    return answer
