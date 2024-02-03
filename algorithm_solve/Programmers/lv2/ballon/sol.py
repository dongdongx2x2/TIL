# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    if len(a) <= 2:
        return len(a)

    answer = 2
    left_min = a[0]
    right_min = a[-1]
    left_idx = 1
    right_idx = len(a) - 2

    while left_idx <= right_idx:
        if left_min < right_min:
            if a[right_idx] < right_min:
                right_min = a[right_idx]
                answer += 1
            right_idx -= 1
        else:
            if a[left_idx] < left_min:
                left_min = a[left_idx]
                answer += 1
            left_idx += 1

    return answer