import sys
sys.stdin = open('25192_input.txt')

input = sys.stdin.readline

n = int(input())
gom = set()
cnt = 0

for _ in range(n):
    user = input().rstrip()

    if user == "ENTER":
        cnt += len(gom)
        gom = set()
    else:
        gom.add(user)

cnt += len(gom)
print(cnt)