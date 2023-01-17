# 숫자를 2 번 입력받기

a= int(input()) # 정수형으로 변환
b = int(input())

print(a + b)


# 점심메뉴 dictionary로 만들기

launch_menu = {'rice': 1000, 'kimch': 1500, 'noodle': 2000}

total_price = 0
for price in launch_menu:
    total_price += launch_menu[price]

print(total_price / len(launch_menu))


