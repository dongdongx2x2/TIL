import sys
sys.stdin = open('input.txt')

def BFS(start):
    visited = [0] * (V + 1)

    visited[start] = 1
    queue = [start]

    while queue:
        start = queue.pop(0)

        if start == G:
            return visited[start] -1

        for next in range(1, V+1):
            if matrix[start][next] and not visited[next]:
                visited[next] = visited[start] + 1
                queue.append(next)
    return 0

T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split()) #V: 노드 개수 #E: 간선의 개수

    matrix = [[0] * (V+1) for _ in range(V+1)]



    for _ in range(E):  # x, y는 연결된 노드 정보
        x, y = map(int, input().split())
        matrix[x][y] = 1
        matrix[y][x] = 1

    # for i in matrix:
    #     print(*i)

    S, G = map(int, input().split()) #S:출발 노드 G: 도착 노드
    # print(S,G)

    print(f'#{tc} {BFS(S)}')
