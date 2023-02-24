import sys
# sys.stdin = open('2491_input.txt')

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

# print(data)


lst = []

cnt = 1
for i in range(len(data)-1):  # 오름차순 계산해보자
    if data[i] <= data[i+1]:
        cnt += 1
    elif data[i] > data[i+1]:
        lst.append(cnt)
        cnt = 1
lst.append(cnt)
cnt2 = 1
for i in range(len(data)-1):
    if data[i] >= data[i+1]:
        cnt2 += 1
    elif data[i] < data[i+1]:
        lst.append(cnt2)
        cnt2 = 1
lst.append(cnt2)
print(max(lst))