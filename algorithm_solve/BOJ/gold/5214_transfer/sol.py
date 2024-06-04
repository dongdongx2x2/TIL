import sys
sys.stdin = open('5214_input.txt')

input = sys.stdin.readline

from collections import deque, defaultdict

def bfs(start):
    visited_stations = [False] * (n + 1)
    visited_tubes = [False] * (m + 1)
    queue = deque([(start, 1)])  # (current station, count of stations visited)
    visited_stations[start] = True

    while queue:
        current_station, count = queue.popleft()

        if current_station == n:  # reached the destination
            return count

        for tube in station_to_tubes[current_station]:
            if not visited_tubes[tube]:
                visited_tubes[tube] = True
                for next_station in tubes[tube]:
                    if not visited_stations[next_station]:
                        visited_stations[next_station] = True
                        queue.append((next_station, count + 1))

    return -1

n, k, m = map(int, input().split())

station_to_tubes = defaultdict(list)
tubes = []

for i in range(m):
    tube = list(map(int, input().split()))
    tubes.append(tube)
    for station in tube:
        station_to_tubes[station].append(i)

print(bfs(1))