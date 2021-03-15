# 문제 : 한 사용자가 회원가입을 하려고 합니다. 회원가입은 이름, 나이, 아이디, 비밀번호 총 4개의 인자를 받습니다. 
# 나이가 20세 이상이면 성인유저, 20세 미만이면 학생유저여야 합니다. 또 블랙리스트라는 제한된 아이디가 담긴 리스트에 요청받은 아이디가 없어야하며, 
# 비밀번호의 길이는 4자 이상이어야 합니다.
# 위 조건들을 통과했을때 회원가입한 유형과 성공실패 여부를 반환하는 함수를 만들어주세요 
# (나이 검사 함수, 아이디 검사 함수, 비밀번호 검사 함수를 포함한 총 4개의 함수를 만들어 주세요)

# 나이 검사 함수 
def age_check(age):
    if int(age) >= 20:
        result = '성인'
    elif int(age) < 20:
        result = '학생' 
    return result

# 아이디 검사 함수 : 아이디가 블랙리스트에 없으면 True반환, 있으면 False반환
def id_check(id):
    black_list_ids = ['black1', 'black2', 'black3']
    if id in black_list_ids:
        return False
    else:
        return True


# 비밀번호 검사 함수 : 비밀번호가 4자 이상이면 True반환, 미만이면 False반환
def password_check(password):
    if len(password) >= 4:
        return True
    else:
        return False

#회원가입 함수 : 나이검사, 아이디검사, 비밀번호검사 함수를 통해 다 통과하면 회원가입 성공, 하나라도 통과못하면 실패
def user_register(user_id, password):
    passing_register = 0 # 0이면 통과 1이면 실패
    if id_check(user_id) == False:
        print(f'{user_id}는 차단된 사용자 입니다.')
        passing_register = 1
    
    if password_check(password) == False:
        print(f'비밀번호는 4자리 이상으로 입력해주세요.')
        passing_register = 1

    if passing_register == 1:
        return False
    elif passing_register == 0:
        return True

# user_login
input_name = input('이름을 입력하세요 : ')
input_age = input('나이를 입력하세요 : ')
input_id = input('아이디를 입력하세요 : ')
input_password = input('비밀번호를 입력하세요 : ')
print('_____________________________________')

user_checker = user_register(input_id, input_password)
user_age = age_check(input_age)


if user_checker == True: # 회원가입 성공
    print(f'{input_name}님의 가입이 성공하였습니다.')
    print(f'{user_age }회원 로그인 정보 : ID : {input_name} password : {input_password}')
elif user_checker == False: # 회원가입 실패
    print(f'{input_name}님 죄송합니다. 재시도 해주세요.')
