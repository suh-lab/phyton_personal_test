class CitizenNumber:

    def __init__(self, number):
        number_store = list()
        for i in range(0, len(number)):
            number_store.append(number[i])
        print(number_store)
        if len(number) == 14:
            for i in range(9, len(number_store)):
                number_store[i] = '*'
            print(number_store)
            number = number_store[0]
            for i in range(1, len(number_store)):
                number += number_store[i]
            print(number)
            self.check = 1
            self.number_store = number_store
        else:
            print("!유효한 주민등록 번호를 입력해주세요\n")
    
    def age_birth_calculator(self, number):
        if self.check == 1:
            age = 2021 - int('10' + number[0] + number[1]) - 900 
            birth_month = self.number_store[2] + self.number_store[3]
            birth_date = self.number_store[4] + self.number_store[5]
            print(age, birth_month, birth_date)

CitizenNumber('980216-1933310').age_birth_calculator('980216-1933310')