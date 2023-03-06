import sys
sys.stdin = open('10431_input.txt')

input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    student = list(map(int,input().split()))[1:]

    cnt = 0
    for i in range(19):
        for j in range(i, 20):
            if student[i] > student[j]:
                student[i], student[j] = student[j], student[i]
                cnt += 1
    print(f'{tc} {cnt}')