import sys
sys.stdin = open('19942_input.txt')

input = sys.stdin.readline

def dfs(idx, pp, ff, ss, vv, sm_cost, food_lst):
    global min_cost, num_lst

    if pp >= mp and ff >= mf and ss >= ms and vv >= mv:
        if sm_cost < min_cost:
            min_cost = sm_cost
            num_lst = [food_lst]
        elif sm_cost == min_cost:
            num_lst.append(food_lst)
        return

    if sm_cost > min_cost:
        return

    if idx == n:
        return

    # 현재 식재료를 선택하는 경우
    dfs(idx + 1, pp + food[idx][0], ff + food[idx][1], ss + food[idx][2], vv + food[idx][3], sm_cost + food[idx][4],
        food_lst + [idx + 1])

    # 현재 식재료를 선택하지 않는 경우
    dfs(idx + 1, pp, ff, ss, vv, sm_cost, food_lst)

n = int(input())
mp, mf, ms, mv = map(int, input().split())

food = []
for _ in range(n):
    tem = list(map(int, input().split()))
    food.append(tem)

min_cost = 1e9
num_lst = []

dfs(0, 0, 0, 0, 0, 0, [])
for lst in num_lst:
    lst.sort()
num_lst.sort()
if min_cost == 1e9:
    print(-1)
else:
    print(min_cost)
    print(*num_lst[0])