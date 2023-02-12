# 1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
# 3의 배수는 출력하지 않는다.


n = int(input())


cnt = 0
while cnt < n:
    cnt += 1
    if cnt % 3 == 0:
        continue
    print(cnt)

