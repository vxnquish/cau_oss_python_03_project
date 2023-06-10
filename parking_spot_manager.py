class parking_spot:
    def __init__(self, name, city, district, ptype, longitude, latitude): # 생성자
        self.__item = {'name': name, 'city': city, 'district': district, 'ptype': ptype, 'longitude': longitude, 'latitude': latitude}

    def get(self, keyword = 'name'): # get 함수
        return self.__item[keyword]

    def __str__(self): # 문자열로 변환할 때 수행할 내용
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
def str_list_to_class_list(str_list):
    class_list = list()
    for i in str_list:
        spl = str(i).split(',') # str_list 의 원소인 문자열 i 를 , (쉼표) 를 기준으로 split 하고, 이를 spl 에 저장한다.
        class_list.append(parking_spot(spl[1], spl[2], spl[3], spl[4], float(spl[5]), float(spl[6]))) # spl[0] 은 [순번] 이므로 제외함.
    return class_list

def print_spots(spots): # parking_spot 클래스의 __str__ 을 이용하여 출력한다.
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(str(spot))

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)