def start():
    day = 0
    list1 = list()
    for i in range(0, 5):
        day = day_count(day)
        store = write_diary(day)
        list1 = dict_to_list(list1, store)
    return list1

def write_diary(day):
    comment = input(f'{day}일의 일기를 입력하세요 : ')
    store = {
        'day' : day,
        'content' : comment
    }
    # print(store)
    return store

def dict_to_list(store_list, dict1):
    store_list.append(dict1)
    return store_list

def day_count(day):
    day = day + 1
    return day

def finder(day_list):
    find_id = input("원하시는 날짜를 입력하세요 : ")
    for i in day_list:
        if int(find_id) in i.values():
            return i['content']
    return "관련한 정보가 없습니다."    

lista = start()
print(finder(lista))

