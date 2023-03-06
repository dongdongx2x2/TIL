# h, b, c, s 가 공백을 두고 입력된다.
# h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수

h, b, c, s = map(int, input().split())

print(round(h*b*c*s/8/1024/1024, 1), 'MB')