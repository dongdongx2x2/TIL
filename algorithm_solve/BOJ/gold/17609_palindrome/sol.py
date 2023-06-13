import sys
sys.stdin = open('17609_input.txt')

input = sys.stdin.readline

def solve(word):
    if word == word[::-1]:
        return 0  # 단어를 뒤집었을 때 바로 회문인지

    s = 0
    e = len(word)-1

    while s < e: # 시작 포인트가 끝 포인트 넘어갈 때 까지
        if word[s] == word[e]: #같으면 계속 하나식 증가 및 감소
            s += 1
            e -= 1
        else:
            tem1 = word[:e] + word[e+1:]
            tem2 = word[:s] + word[s+1:]

            if tem1 == tem1[::-1] or tem2 == tem2[::-1]:
                return 1

            return 2


T = int(input())

for _ in range(T):
    word = input().rstrip()
    print(solve(word))




