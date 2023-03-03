import sys
sys.stdin = open('5178_input.txt')



T = int(input())

for tc in range(1, T+1):

    # N:총 노드의 개수 M:리프노드개수 L:출력할노드
    N, M, L = map(int,input().split())

    Tree = [0] * (N+1)

    for _ in range(M):
        a, b = map(int,input().split())
        # a는 리프노드 번호 b는 a에들어가야할 자연수
        Tree[a] = b

    # print(Tree)

    if len(Tree) % 2 == 0:
        for i in range(N-M, 0, -1):
            Tree[i] = Tree[i*2] + Tree[i*2+1]
    else:
        for i in range(N-M-1, 0, -1):
            Tree[i] = Tree[i * 2] + Tree[i * 2 + 1]
            Tree[N//2] = Tree[N]

    print(f'#{tc} {Tree[L]}')
