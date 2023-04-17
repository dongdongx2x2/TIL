import sys
sys.stdin = open('1197_input.txt')

input = sys.stdin.readline

# 대표 원소 정리
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

# 집합 생성
def union(x, y):
    a = find_set(x)
    b = find_set(y)

    if b < a:
        parent[a] = b

    else:
        parent[b] = a

# 노드, 간선
V, E = map(int, input().split())
# 간선 정보
edge = [list(map(int, input().split())) for _ in range(E)]
# 가중치 기준 정렬
edge.sort(key=lambda x : x[2])

# 대표 원소 정보
parent = list(range(V+1))
result = 0
for s, e, w in edge:
    # 사이클을 형성하지 않도록 대표원소 정보가 다를떄만
    if find_set(s) != find_set(e):
        union(s, e)     # 집합 형성
        result += w     # 가중치 합
print(result)

