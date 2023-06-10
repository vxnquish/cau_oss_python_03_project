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

        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")

        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")

        elif select == 4:
            print("Exit")   # 4 를 입력했을 경우,
            break           # Exit 을 출력하고,
                            # 반복문을 빠져나가 함수를 종료한다.

        else:
            print("invalid input")