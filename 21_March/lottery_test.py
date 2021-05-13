# 1-45 까지 랜덤한 숫자 7개를 받는 로또 번호 예측 프로그램 만들기
# 중복되는 숫자는 제외하고 출력하며 출력이 끝나고 다시 실행할 수 있게 만들자

import random

class Lottery:
    def __init__(self):
        lottery_number = list()
        while len(lottery_number) != 7:
            number = random.randrange(1, 45)
            if number in lottery_number:
                pass
            else:
                lottery_number.append(random.randrange(1, 45))
        lottery_number = sorted(lottery_number)
        print('\n로또 예상 번호')
        print(f'{lottery_number[0]} {lottery_number[1]} {lottery_number[2]} {lottery_number[3]} {lottery_number[4]} {lottery_number[5]} + {lottery_number[6]}')

# return값 반환 개념?

loop = 1
# while loop != 'exit':
#     loop = input('\nexit이나 0을 입력하면 나갑니다 : ')
#     if loop == 'exit':
#         break
#     Lottery()
            
# 재귀호출
def test():
    loop = input('\nexit이나 0을 입력하면 나갑니다 : ')
    if loop != 'exit': 
        Lottery()
        test()

test()