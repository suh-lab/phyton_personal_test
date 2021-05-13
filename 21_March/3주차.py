class UserDelete:

    def __init__(self, current_password="123"): # 현재 유저의 비밀번호 먼저 생성
        self.current_password = current_password

    def user_password_check(self, input_password): # 함수에 들어온 password 값이 초기에 생성된 비밀번호와 일치 여부를 확인하여 반환하는 클래스
        result = False
        if input_password == self.current_password:
            result = True
        return result

    # def output_result(self, result):
    #     if result == True:
    #         print('탙퇴 완료')
    #     else:
    #         print('탙퇴 실패')


input_password = input('탈퇴를 위해 비밀번호를 입력해주세요 : ')
result = UserDelete().user_password_check(input_password=input_password)
# UserDelete().output_result(result

if result:
    print("탈퇴 실패")
else:
    print("탈퇴 완료")
