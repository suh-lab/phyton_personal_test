# nums = [20, 40, 50]
nums = [70, 70, 10]
ranks = [0, 0, 0]


#1순위
for ranks_num in range(0,2):
    if nums[0] >= nums[1] and nums[0] >= nums[2]:
        ranks[0] = 1
        first_num = nums[0]
    elif nums[1] >= nums[0] and nums[1] >= nums[2]:
        ranks[1] = 1
        first_num = nums[1]
    elif nums[2] >= nums[0] and nums[2] >= nums[1]:
        ranks[2] = 1
        first_num = nums[2]

# 3순위
for ranks_num in range(0,2):
    if nums[0] <= nums[1] and nums[0] <= nums[2]:
        ranks[0] = 3
        third_num = nums[0]
    elif nums[1] <= nums[0] and nums[1] <= nums[2]:
        ranks[1] = 3
        third_num = nums[1]
    elif nums[2] <= nums[0] and nums[2] <= nums[1]:
        ranks[2] = 3
        third_num = nums[2]

# 2순위 정하기
for ranks_num in range(0,2):
    if nums[0] < first_num and nums[0] > third_num:
        ranks[0] = 2
        second_num = nums[0]
    elif nums[1] < first_num and nums[1] > third_num:
        ranks[1] = 2
        second_num = nums[1]
    elif nums[2] < first_num and nums[2] > third_num:
        ranks[2] = 2    
        second_num = nums[2]
    else:
        second_num = 0

# 비교 대상의 값이 같을때 순위 설정
#1순위
if first_num == nums[0]:
    ranks[0] = 1
if first_num == nums[1]:
    ranks[1] = 1
if first_num == nums[2]:
    ranks[2] = 1
#2순위
if second_num == nums[0]:
    ranks[0] = 2
if second_num == nums[1]:
    ranks[1] = 2
if second_num == nums[2]:
    ranks[2] = 2

print(f'초기 숫자 : {nums}')
print(f'숫자 순위 : {ranks}')