import sys
sys.stdin = open('15686_input.txt')

input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# print(v)
house = []
chics = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            chics.append((i,j))

mx = 1000000
for chic in combinations(chics, M): # 치킨 집들중 M개 각각 홈들이랑 거리 비교
    city_dis = 0
    for k in house: # 집들 하나하나
        dis = 1000000
        for i in chic: # 치킨집들 하나하 나
            dis = min(dis, abs(k[0]-i[0]) + abs(k[1]-i[1]))
        city_dis += dis
    mx = min(mx, city_dis)
print(mx)

