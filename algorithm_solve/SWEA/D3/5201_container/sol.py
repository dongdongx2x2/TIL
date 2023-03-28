import sys
sys.stdin = open('5201_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    cons = list(map(int, input().split()))
    cons.sort()
    trucks = list(map(int, input().split()))
    trucks.sort()

    result = 0
    while cons and trucks:
        con = cons.pop()
        truck = trucks.pop()

        if truck >= con:
            result += con
        else:
            trucks.append(truck)

    print(f'#{tc} {result}')



