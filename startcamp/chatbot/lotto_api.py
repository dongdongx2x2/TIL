# 파이썬으로 웹 요청 보낼수 있는 라이브러리 불러오기
import requests

# (회차 직접 입력)
turn = input('회차를 입력하시오:')
# 동행복권 로또 당첨 번호 api 사용하기
url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={turn}'

# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스번호 제외)
r = requests.get(url).json()

numbers = list(range(1,7))

lotto_list = []
for no in numbers:
    #print(r[f'drwtNo{no}'])
    lotto_list.append(r[f'drwtNo{no}'])

print(lotto_list)
# 4. 이걸 1000번 반복한다.
    # 1. 로또 번호 6개를 추첨 받는다.
    # 2. 내가 추첨 받은 6개의 번호가 1049회차 번호와 일치 하는지 확인한다.
        # 2-1. 확인하는 방법은 내 번호 6개를 순회하면서 
            # 1049회 당첨번호 목록에 해당 숫자가 있는지
            # 있다면 적중 횟수 + 1
    # 3. 그래서 적중 횟수가 6개면 1등
        # 5개면 3등
        # 4개면 4등
        # 3개면 5등
        # 2개 이하면 꽝을 출력한다.

import random
for _ in range(1000):
    lotto_numbers = list(range(1,46))

    my_numbers =random.sample(lotto_numbers,6)
    a = 0
    for i in my_numbers:
        if i in lotto_list:
            a = a + 1
    if a == 6:
        print('1등')
    elif a == 5:
        print('3등')
    elif a == 4:
        print('4등')
    elif a == 3:
        print('5등')
    else:
        print('꽝')
                        
        
      