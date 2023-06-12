import sys
sys.stdin = open('22251_input.txt')

input = sys.stdin.readline

N, K, P, X = map(int,input().split())

# N 층까지 용
# K 자리수
# P 최대 반전
# X 현재 층수

# 0-1 4개  1-2 5개 2-3 2개 3-4 3개 4-5 3개 5-6 1개 6-7 5개 7-8 4개 8-9 1개
# 0-2 3개  1-3 3개 2-4 5개 3-5 2개 4-6 4개 5-7 4개 6-8 1개 7-9 3개
# 0-3 3개  1-4 2개 2-5 4개 3-6 3개 4-7 3개 5-8 2개 6-9 2개
# 0-4 4개  1-5 5개 2-6 3개 3-7 2개 4-8 3개 5-9 1개
# 0-5 3개  1-6 6개 2-7 4개 3-8 2개 4-9 2개
# 0-6 2개  1-7 1개 2-8 2개 3-9 1개
# 0-7 3개  1-8 5개 2-9 3개
# 0-8 1개  1-9 4개
# 0-9 2개

num = {
    0: [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    1: [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    2: [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    3: [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    4: [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    5: [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    6: [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    7: [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    8: [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    9: [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
}

# print(str(X).zfill(K))
# goal_num = str(X).zfill(K)
#
# for i in goal_num:
#     change_num = num[int(i)]
#     print(i)

def solve(idx, temp, su, cnt):
    if cnt > P or su > N:
        return 0

    if idx == K:
        if su != 0:
            return 1
        return 0

    result = 0
    for i in range(10):
        result += solve(idx + 1, temp * 10, i * temp + su, cnt + num[X // temp % 10][i])

    return result

result = solve(0, 1, 0, 0)
print(result - 1)