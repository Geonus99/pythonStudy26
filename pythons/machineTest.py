# 커피 자판기

# 판매자모드 / 소비자모드
# 결제 방식 : 현금, 카드, 페이, 교통카드
# 상품
# + 커피류 : 아메리카노, 카페라떼, 콜드브루, 카페모카, 카푸치노, 아샷추, 카라멜 마키아또
# + 티 : 히비스커스티, 얼그레이 밀크티, 아쌈 밀크티, 녹차, 캐모마일차
# + Non-커피 : 핫초코, 말차라떼, 말차초코라떼, 율무차, 미숫가루, 따뜻한 우유
# + 음료수 : 사이다, 콜라, 포카리스웨트, 게토레이, 헛개차, 물
# 옵션
# + 커피류 : 디카페인 여부, 샷추가, 시럽유무, Hot/Ice, 설탕
# + 티 : 샷추가, Hot/Ice, 설탕
# + Non-커피 : 샷추가, Hot/Ice, 설탕

items = [ # name, price, options
    {
        "name": '커피류',
        "items": [
            {"name": '아메리카노', "price": 1500, 'options': ['decaf', "shot", 'syrup', 'hot/ice', 'sugar']},
            {"name": '카페라떼', "price": 2500, 'options': ['decaf', "shot", 'syrup', 'hot/ice', 'sugar']},
            {"name": '콜드브루(ICE만)', "price": 3000, 'options': ['decaf', "shot", 'syrup', 'sugar']},
            {"name": '카페모카', "price": 3000, 'options': ['decaf', "shot", 'syrup', 'hot/ice', 'sugar']},
            {"name": '카푸치노', "price": 3000, 'options': ['decaf', "shot", 'syrup', 'hot/ice', 'sugar']},
            {"name": '아샷추', "price": 3000, 'options': ['decaf', "shot", 'syrup', 'hot/ice', 'sugar']},
            {"name": '카라멜 마키아또', "price": 5000, 'options': ['decaf', "shot", 'syrup', 'hot/ice', 'sugar']},
        ]
    },
    {
        "name": "티",
        "items": [
            {"name": '히비스커스티', "price": 2000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '얼그레이 밀크티', "price": 3000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '아쌈 밀크티', "price": 3000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '녹차', "price": 2000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '캐모마일차', "price": 2000, 'options': ["shot", 'hot/ice', 'sugar']},
        ]
    },
    {
        'name': 'Non-커피',
        'items': [
            {"name": '핫초코', "price": 4000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '말차라떼', "price": 4000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '말차초코라떼', "price": 4500, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '율무차', "price": 3000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '미숫가루', "price": 5000, 'options': ["shot", 'hot/ice', 'sugar']},
            {"name": '따뜻한 우유', "price": 2000, 'options': ["shot", 'hot/ice', 'sugar']},
        ]
    },
    {
        'name': '음료수',
        'items': [
            {"name": '사이다', "price": 6000, 'options': []},
            {"name": '콜라', "price": 6000, 'options': []},
            {"name": '포카리스웨트', "price": 7000, 'options': []},
            {"name": '게토레이', "price": 7000, 'options': []},
            {"name": '헛개차', "price": 6000, 'options': []},
            {"name": '물', "price": 2000, 'options': []},
        ]
    }
]

options = { # name, price, type
    "decaf": {'name': '디카페인', "price": 500, 'type': 'bool'},
    "shot": {'name': '샷추가', "price": 500, 'type': 'range'},
    'syrup': {'name': '시럽', 'price': 500, 'type': 'range'},
    'hot/ice': {'name': 'HOT -> ICE', 'price': 500, 'type': 'bool'},
    'sugar': {'name': '설탕', 'price': 500, 'type': 'range'},
}

convert_options = {'디카페인': 'decaf', '샷추가': 'shot', '시럽': 'syrup', 'HOT -> ICE': 'hot/ice', '설탕': 'sugar'}

intro_message = """
================================
커피 자판기에 오신것을 환영합니다.
================================
"""

# 메뉴
intro_menu = ['소비자 모드', '자판기 종료']

def print_menu(menu_title, menu_list, message=None):
    print(f'{menu_title:-^32}')
    if message: print(f'{message}'); print('-' * 34)
    for idx, item in enumerate(menu_list):
        print(f'{idx + 1}. {item}')

def print_selected_options(selected_options):
    if selected_options.get('decaf'):
        decaf_str = "함"
    else:
        decaf_str = '안함'
    print(f'ㄴ 디카페인(+500원) : {decaf_str}', end=" | ")
    shot = selected_options.get('shot')
    print(f'샷추가(샷당 +500원) : {shot}샷', end=" | ")
    syrup = selected_options.get('syrup')
    print(f'시럽(회당 +500원) : {syrup}회', end=" | ")
    if selected_options.get('hot/ice'):
        hot_ice_str = "아이스"
    else:
        hot_ice_str = '핫'
    print(f'Hot/Ice(+500원) : {hot_ice_str}', end=" | ")
    sugar = selected_options.get('sugar')
    print(f'설탕(개당 +500원) : {sugar}개')

def input_number(max_number):
    num = input(f'1~{max_number}의 숫자를 입력하세요 : ')
    while not num.isdigit() or int(num) not in range(1, max_number + 1):
        print('잘못입력하셨습니다.')
        num = input(f'1~{max_number}의 숫자를 입력하세요 : ')
    return int(num)

def input_money():
    money = input('금액을 입력해주세요 : ')
    while not money.isdigit() or not int(money) > 0:
        print('잘못입력하셨습니다.')
        money = input('금액을 입력해주세요 : ')
    return int(money)

def input_yn():
    yn = input('확정하시겠습니까(y/n)? : ')
    while yn.lower() not in ['y', 'n']:
        print('잘못입력하셨습니다.')
        yn = input('확정하시겠습니까(y/n)? : ')
    return yn == 'y'

def main():
    global items, options
    print(intro_message)
    run = True
    while run:
        print_menu('메인', intro_menu)
        num = input_number(len(intro_menu))
        if num == 1:
            # 소비자 모드
            run_customer_mode = True
            selected_items = []
            while run_customer_mode:
                customer_menu = [item.get('name') for item in items]
                customer_menu.append('결제하기')
                customer_menu.append('뒤로가기')
                print_menu('자판기', customer_menu, '구매하실 상품군을 선택해 주세요!')
                num = input_number(len(customer_menu))

                if num == len(customer_menu) - 1:
                    # 선택된 메뉴 출력
                    total_price = 0
                    if len(selected_items) == 0:
                        print('상품을 선택해주세요.')
                    else:
                        print('=' * 34)
                        print('선택된 메뉴 리스트')
                        for selected_item in selected_items:
                            item = selected_item.get('item')
                            name = item.get('name')
                            price = item.get('price')
                            print('-' * 33)
                            print(f'+ {name}({price:,}원)')
                            option = selected_item.get('option')
                            if len(item.get('options')) > 0:
                                print_selected_options(option)
                        for selected_item in selected_items:
                            item = selected_item.get('item')
                            price = item.get('price')
                            total_price += price
                            option = selected_item.get('option')
                            is_decaf = option.get('decaf', False)
                            shot = option.get('shot', 0)
                            syrup = option.get('syrup', 0)
                            hot_ice = option.get('hot/ice', False)
                            sugar = option.get('sugar', 0)
                            total_price += 500 if is_decaf else 0
                            total_price += shot * 500
                            total_price += syrup * 500
                            total_price += 500 if hot_ice else 0
                            total_price += sugar * 500
                        print('-' * 34)
                        print(f'* 총 금액 : {total_price:,}원')
                        print('=' * 34)
                        purchase_menu = ['카드결제', '현금결제', '교통카드']
                        print_menu('결제하기', purchase_menu, '결제할 수단을 고르세요.')
                        num_purchase = input_number(len(purchase_menu))
                        if num_purchase == 1:
                            print('카드 한도를 입력해주세요.')
                        elif num_purchase == 2:
                            print('남아있는 현금의 금액을 입력해주세요.')
                        elif num_purchase == 3:
                            print('충전되어 있는 교통카드의 잔액을 입력해주세요.')
                        money = input_money()
                        if money >= total_price:
                            money = money - total_price
                            print(f'* 결제 금액 : {total_price:,}원')
                            print(f'* 잔액 : {money:,}원')
                            print('정상적으로 결제 되었습니다.')
                            print('=' * 34)
                            selected_items = []
                        else:
                            print('잔액이 부족합니다.')
                            print('처음 메뉴로 이동합니다.')
                    continue
                if num == len(customer_menu):
                    run_customer_mode = False
                    continue
                run_menu_mode = True
                while run_menu_mode:
                    menu = []
                    for item in items[num - 1].get('items'):
                        menu.append(f'{item.get("name")}({item.get("price"):,}원)')
                    menu.append('뒤로가기')
                    print_menu(customer_menu[num - 1], menu, '메뉴를 선택해주세요!')
                    num_menu = input_number(len(menu))
                    if num_menu == len(menu):
                        run_menu_mode = False
                        continue
                    run_detail_mode = True
                    total_price = 0
                    selected_menu = items[num - 1].get('items')[num_menu - 1]
                    # total_price += selected_menu.get('price')
                    if len(selected_menu.get('options')) > 0: # 옵션이 있을 경우
                        selected_options = {
                            'decaf': False,
                            'shot': 0,
                            'syrup': 0,
                            'hot/ice': False,
                            'sugar': 0
                        }
                        while run_detail_mode:
                            details = [options[option].get('name') for option in selected_menu.get('options')]
                            details.append('선택완료')
                            details.append('뒤로가기')
                            detail_menu = []
                            for detail in details:
                                if detail == '뒤로가기' or detail == '선택완료':
                                    detail_menu.append(detail)
                                    continue
                                detail_str = f'{detail}(+{options.get(convert_options.get(detail)).get("price"):,}원)'
                                detail_menu.append(detail_str)
                            print_menu(selected_menu.get('name'), detail_menu, '옵션을 선택해주세요!')
                            num_details = input_number(len(detail_menu))
                            if num_details == len(detail_menu): # 뒤로가기
                                run_detail_mode = False
                                continue
                            if num_details == len(detail_menu) - 1: # 선택완료
                                menu_name = selected_menu.get('name')
                                print(f'+ {menu_name}')
                                print_selected_options(selected_options)
                                if input_yn():
                                    print('선택이 완료되었습니다.')
                                    selected_items.append({
                                        'item': selected_menu,
                                        'option': selected_options
                                    })
                                    run_detail_mode = False
                                    run_menu_mode = False
                                else:
                                    print('선택이 취소되었습니다.')
                                    run_detail_mode = False
                                continue
                            current_option = convert_options[details[num_details - 1]]
                            temp = options[current_option]
                            name = temp.get('name')
                            if temp.get('type') == 'bool':
                                selected_options[current_option] = True
                                print(f'{name} 옵션이 추가되었습니다.')
                            elif temp.get('type') == 'range':
                                print('추가할 양을 입력하세요.')
                                amount = input_number(5)
                                selected_options[current_option] = amount
                                print(f'{name}: {amount} 양만큼 추가')
                    else:
                        # 옵션이 없을 경우
                        selected_items.append({
                            'item': selected_menu,
                            'option': {}
                        })
                        name = selected_menu.get('name')
                        print(f'{name}이 선택되었습니다.')
                        run_menu_mode = False

                # 선택된 메뉴 출력
                if len(selected_items) > 0:
                    print('=' * 34)
                    print('선택된 메뉴 리스트')
                    for selected_item in selected_items:
                        item = selected_item.get('item')
                        name = item.get('name')
                        price = item.get('price')
                        print('-' * 33)
                        print(f'+ {name}({price:,}원)')
                        option = selected_item.get('option')
                        if len(item.get('options')) > 0:
                            print_selected_options(option)
                    print('=' * 34)
        elif num == len(intro_menu):
            # 프로그램 종료
            print('=' * 32)
            print('자판기를 종료합니다.')
            print('=' * 32)
            run = False

if __name__ == "__main__":
    main()