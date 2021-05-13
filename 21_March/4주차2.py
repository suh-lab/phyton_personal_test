# 문제: RandomNumber라는 클래스를 만듭니다. RandomNumber가 호출 될 때마다 
# 1부터 10사이의 수 중 10개의 int형 숫자가 랜덤하게 들어 있는 numbers라는 리스트를 생성합니다. 
# RandomNumber 내에 함수를 하나 정의하고 그 함수에서 check_num이라는 숫자를 인자로 받고, 
# 생성된 numbers 리스트 내에서 check_num보다 작거나 같은 숫자들을 내림차순으로 정렬된 리스트로 반환하는 로직을 정의해주세요.
# (해결하시면 출력된 결과를 중복 제거하고 출력되게도 도전해보세요!)

# 입력 예시 ) result = RandomNumber().check_num(5)   # 랜덤하게 생성된 숫자 리스트는 [2, 3, 5, 7, 8, 9, 1, 2, 3, 4]
# 출력 예시 ) [5, 4, 3, 3, 2, 2, 1]
# 중복제거 출력 예시 ) [5, 4, 3, 2, 1]

# * 1부터 10사이의 랜덤한 숫자를 생성하는 방법은 아래를 참고해주세요.
# import random

# random_num = random.randrange(1, 10)

import random

class RandomNumber:
    def __init__(self):
        self.numbers = list()
        for count in range(0, 10): 
            random_number = random.randrange(1, 10)
            self.numbers.append(random_number)
        print("기존 리스트 : ", self.numbers) 

    def rearrange(self, limit_num):
        output_list = list()
        for count in range(0, len(self.numbers)):
            if self.numbers[count] <= int(limit_num):
                if self.numbers[count] in output_list:
                    pass
                else:
                    output_list.append(self.numbers[count])
        print("변환 리스트 : ", sorted(output_list))
            
limit_num = input("입력한 수의 이하만 출력하여 정렬합니다 : ")
RandomNumber().rearrange(limit_num)

import random


# class RandomNumber:

#     def __init__(self):
#         self.numbers = list()
#         for i in range(10):
#             self.numbers.append(int(random.randrange(1, 10)))

#     def distinct_number(self, check_numbers:list):
#         distinct_numbers = list()
#         if check_numbers:
#             for num in check_numbers:
#                 if num not in distinct_numbers:
#                     distinct_numbers.append(num)
#         return distinct_numbers

#     def check_number(self, check_num:int):
#         check_numbers = list()
#         if check_num:
#             for num in self.numbers:
#                 if check_num <= num:
#                     check_numbers.append(num)
#         result = self.distinct_number(check_numbers=check_numbers)
#         return sorted(result)

# print(RandomNumber().check_number(5))