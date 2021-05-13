class CellPhone:

    # def check_phonenumber(self, number:int):
    #     if type(number) != int:
    #         return False
    #     else:
    #         ~~~~~

    def __init__(self, number):

        number_store = list()
        for i in range(0, len(number)):
            number_store.append(number[i])
        # if number[0] == '0' and number[1] == '1' and len(number) == 11:
        if number[0:2] == '01' and len(number) == 11:
            for i in range(3, 7):
                number_store[i] = '*'
            number = '0'
            for i in range(1, len(number_store)):
                number += number_store[i]
            print(number)
        else:
            print("\n!정확한 핸드폰 번호를 입력해주세요\n휴대폰 앞 2자리는 01로 시작해야하며 11자리 모두를 입력하셔야 합니다..")


class CitizenNumber:

    def __init__(self, number):
        number_store = list()
        for i in range(0, len(number)):
            number_store.append(number[i])
        if len(number) == 14:
            for i in range(9, len(number_store)):
                number_store[i] = '*'
            number = number_store[0]
            for i in range(1, len(number_store)):
                number += number_store[i]
            self.check = 1
            self.number_store = number_store
            self.number = number
        else:
            self.check = 0
            print("!유효한 주민등록 번호를 입력해주세요\n")
    
    def age_birth_calculator(self, number):
        if self.check == 1:
            age = 2021 - int('10' + number[0] + number[1]) - 900 
            birth_month = self.number_store[2] + self.number_store[3]
            birth_date = self.number_store[4] + self.number_store[5]
            print(f"{self.number} 나이는{age}, {birth_month}월 {birth_date}일생입니다.")


phone_number = input("핸드폰 번호를 입력하세요 : ")
citizen_number = input("주민등록 번호를 입력하세요 : ")

CellPhone(phone_number)
CitizenNumber(citizen_number).age_birth_calculator(citizen_number)