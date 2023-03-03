import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):

    tc, N = input().split()
    num = list(input().split())
    N = int(N)

    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"] # 넘버리스트 만들어줌
    new_list= []
    for i in range(10):
        for j in range(N): # 반복 돌면서 같다면
            if num_list[i] == num[j]:
                new_list.append(num[j]) # 순서대로 뉴리스트에 넣어줌
    print(f'{tc}')
    print(*new_list)


