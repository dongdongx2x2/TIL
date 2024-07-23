import sys, heapq
sys.stdin = open('18223_input.txt')

input = sys.stdin.readline

def dijk(start):
    distances = [INF] * (v + 1)
    distances[start] = 0
    q = [(0, start)]

    while q:
        cur_distance, cur_node = heapq.heappop(q)

        if distances[cur_node] < cur_distance:
            continue

        for neighbor, weight in graph[cur_node]:
            distance = cur_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(q, (distance, neighbor))
    return distances


v, e, p = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

all = dijk(1)
gunwoo = dijk(p)

start_to_masan = all[v]
start_to_gunwoo_to_masan = all[p] + gunwoo[v]

if start_to_masan == start_to_gunwoo_to_masan:
    print("SAVE HIM")
else:
    print("GOOD BYE")