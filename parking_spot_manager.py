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

# Version #2
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

# Version #3
def filter_by_name(spots, name):
    list = [i for i in spots if name in i.get('name')]                  # 입력받은 문자열이 각 spot 의 'name' 에 포함되면, 
    return list                                                         # 그 해당 spot 으로만 구성된 list 를 생성하고 return 한다. 

def filter_by_city(spots, city):
    list = [i for i in spots if city in i.get('city')]                  # 입력받은 문자열이 각 spot 의 'city' 에 포함되면,
    return list                                                         # 그 해당 spot 으로만 구성된 list 를 생성하고 return 한다. 

def filter_by_district(spots, district):
    list = [i for i in spots if district in i.get('district')]          # 입력받은 문자열이 각 spot 의 'district' 에 포함되면, 
    return list                                                         # 그 해당 spot 으로만 구성된 list 를 생성하고 return 한다. 

def filter_by_ptype(spots, ptype):
    list = [i for i in spots if ptype in i.get('ptype')]                # 입력받은 문자열이 각 spot 의 'ptype' 에 포함되면, 
    return list                                                         # 그 해당 spot 으로만 구성된 list 를 생성하고 return 한다. 

def filter_by_location(spots, locations):
    list = [i for i in spots if locations[0] < i.get('latitude')        # 입력받은 최소/최대 위도, 최소/최대 경도 범위 내에 있는 spot 에 대하여,
                            and locations[1] > i.get('latitude')        # 그 해당 spot 으로만 구성된 list 를 생성하고 return 한다. 
                            and locations[2] < i.get('longitude')                          
                            and locations[3] > i.get('longitude')]
    return list

# Version 4
def sort_by_keyword(spots, keyword):                                    
    return sorted(spots, key = lambda x: x.get(keyword))                # 입력 받은 keyword 를 정렬 기준으로 삼고,
                                                                        # 정렬 된 spots 를 return 한다.