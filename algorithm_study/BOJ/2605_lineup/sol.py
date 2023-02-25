import sys
sys.stdin = open('2605_input.txt')

input = sys.stdin.readline

N = int(input())
student_idx = list(map(int, input().split()))



result = []
for i in range(N):
    result.insert(student_idx[i],i+1)
# print(result)
print(*result[::-1])

