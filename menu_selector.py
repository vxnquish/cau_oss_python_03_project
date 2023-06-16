import file_manager
import parking_spot_manager

def start_process(path):
    temp_list = file_manager.read_file(path) # file_manager.py 에 있는 read_file 함수에서 return 값인 list_str 을 temp_list 에 저장한다.
    main_list = parking_spot_manager.str_list_to_class_list(temp_list)  # parking_spot_manager.py 에 있는
                                                                        # str_list_to_class_list 함수에서
                                                                        # return 값인 class_list 를 main_list 에 저장한다.

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(main_list) # 1 을 입력했을 경우,
                                                        # parking_spot_manager.py 에 있는
                                                        # print_spots 함수를 호출한다.

        elif select == 2:                               # 2 를 입력했을 경우, 
            print("---filter by---")                    # filter 기능을 이용할 수 있다.
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))    # 어떤 방식으로 필터를 할 것인지 입력을 받는다.
            
            if select == 1:
                keyword = input('type name:')                                               # 1 을 입력했을 경우, 문자열을 받아서 keyword 에 저장하고
                main_list = parking_spot_manager.filter_by_name(main_list, keyword)         # parking_spot_manager.py 에 있는 filter_by_name 함수를 호출한다.
                                                                                            # main_list 를 위 함수의 return 값으로 덮어씌운다.

            elif select == 2:
                keyword = input('type city:')                                               # 2 를 입력했을 경우, 문자열을 받아서 keyword 에 저장하고
                main_list = parking_spot_manager.filter_by_city(main_list, keyword)         # parking_spot_manager.py 에 있는 filter_by_city 함수를 호출한다.
                                                                                            # main_list 를 위 함수의 return 값으로 덮어씌운다.
            
            elif select == 3:
                keyword = input('type district:')                                           # 3 을 입력했을 경우, 문자열을 받아서 keyword 에 저장하고
                main_list = parking_spot_manager.filter_by_district(main_list, keyword)     # parking_spot_manager.py 에 있는 filter_by_district 함수를 호출한다.
                                                                                            # main_list 를 위 함수의 return 값으로 덮어씌운다.
                
            elif select == 4:
                keyword = input('type ptype:')                                              # 4 를 입력했을 경우, 문자열을 받아서 keyword 에 저장하고
                main_list = parking_spot_manager.filter_by_ptype(main_list, keyword)        # parking_spot_manager.py 에 있는 filter_by_ptype 함수를 호출한다.
                                                                                            # main_list 를 위 함수의 return 값으로 덮어씌운다.
                
            elif select == 5:
                min_lat = float(input('type min lat:'))                                     # 5 를 입력했을 경우, 최소/최대 위도, 최소/최대 경도를 입력받아
                max_lat = float(input('type max lat:'))                                     # tuple 이라는 튜플에 위의 4개의 값을 순서대로 저장하고, 
                min_lon = float(input('type min long:'))                                    # parking_spot_manager.py 에 있는 filter_by_location 함수를 호출한다.
                max_lon = float(input('type max long:'))                                    # main_list 를 위 함수의 return 값으로 덮어씌운다.
                tuple = (min_lat, max_lat, min_lon, max_lon)
                main_list = parking_spot_manager.filter_by_location(main_list, tuple)

            else:
                print("invalid input")

        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                main_list = parking_spot_manager.sort_by_keyword(main_list, keyword)        # 6개의 keyword 중 하나를 입력하면,
                                                                                            # parking_spot_manager.py 에 있는 sort_by_keyword 함수를 호출한다.
            else: print("invalid input")                                                    # main_list 를 위 함수의 return 값으로 덮어씌운다.

        elif select == 4:
            print("Exit")   # 4 를 입력했을 경우,
            break           # Exit 을 출력하고,
                            # 반복문을 빠져나가 함수를 종료한다.

        else:
            print("invalid input")