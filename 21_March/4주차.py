import random

class RandomNumber:
    
    def __init__(self):
        numbers = list()
        
        for count in range(0, 10):
            random_num = random.randrange(1, 10)
            numbers.append(random_num)

        print("기존 리스트 : ", numbers)
        self.origin_list = numbers

    #밑은 실험한 내용입니다.
    def rearrange_list(self): #오름차순 함수
        origin_list = self.origin_list
        print("정렬 리스트 : ", sorted(origin_list))

    def limit_rearrange_list(self, limit_value): #오름차순 제한
        origin_list = self.origin_list
        arrange_list = list()

        for count in range(0, len(origin_list)):
            if origin_list[count] <= int(limit_value):
                arrange_list.append(origin_list[count])
        print("제한 리스트 : ", sorted(arrange_list))
    
    #밑의 함수만 과제 내용입니다.
    # distinct_limit_list
    def limit_rearrange_list_except_same(self, limit_value): #오름차순 제한 중복제거
        origin_list = self.origin_list
        arrange_list = list()

        for i in range(0, len(origin_list)):
            if origin_list[i] <= int(limit_value):
                if origin_list[i] not in arrange_list:
                    arrange_list.append(origin_list[i])
                # if origin_list[i] in arrange_list:
                #     pass
                # else:
                #     arrange_list.append(origin_list[count])
        print("제한 리스트 : ", sorted(arrange_list))

# 실험할때 쓰였던 호출 코드    
# RandomNumber().rearrange_list()
# limit_num = input("\n입력한 수 이하의 값만 출력합니다 : ")
# RandomNumber().limit_rearrange_list(limit_num)

input_limit_num = input("\n입력한 수 이하의 값만 중복없이 출력합니다 : ")
RandomNumber().limit_rearrange_list_except_sames(input_limit_num)
