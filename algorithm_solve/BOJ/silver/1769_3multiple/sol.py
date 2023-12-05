import sys
sys.stdin = open('1769_input.txt')

input = sys.stdin.readline

X = input().rstrip()
cnt = 0
while len(X) >= 2:
    t = 0
    for i in range(len(X)):
        t += int(X[i])
    X = str(t)
    cnt += 1
print(cnt)
if int(X) % 3 == 0:
    print("YES")
else:
    print('NO')
