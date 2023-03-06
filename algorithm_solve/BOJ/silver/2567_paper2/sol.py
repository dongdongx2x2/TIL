import sys
sys.stdin = open('2567_input.txt')
input = sys.stdin.readline

N = int(input())
arr = [[0]*105 for _ in range(105)] #인덱스 조금더 더해줌

for _ in range(N):
    si, sj = map(int, input().split())

    for i in range(si+1, si+10+1):  # 가쪽에 하는 경우 방지 +1씩해줌
        for j in range(sj+1, sj+10+1):
            arr[i][j] = 1

cnt = 0                 # 사각형 위에서부터 밑으로 내려가며 다음 항목이랑 숫자다른거 세기
for i in range(104):
    temp = 0
    for j in range(104):
        if arr[j][i] != arr[j+1][i]:
            temp += 1
    cnt += temp

for i in range(104):  # 사각형 왼쪽에서 오른쪽으로가며 다음 항목 숫자다르면 세기
    temp = 0
    for j in range(104):
        if arr[i][j] != arr[i][j+1]:
            temp += 1
    cnt += temp
print(cnt)
