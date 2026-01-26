from tabulate import tabulate
# 상품에 대한 crud를 구현해보자
# C -> 새 상품 등록
# R -> 전체상품 목록
# R -> 단일상품 자세히 보기
# U -> 상품 수정
# D -> 상품 품절(매진)

# 사용할 변수 전역변수
run = True

item_names = ["노트북","모니터"] # 상품명
unit_prices = [1200000, 400000] # 단가
quantity = [40, 25] # 수량
product_infor = ["AI용 삼성노트북","LG24인치 LED"] # 상품 정보
categorys = ["가전","잡화"] # 상품 분류
headers = ['No','품명','단가','수량','상세정보','카테고리'] # 조회용테이블 서식
items = zip(range(len(item_names)), item_names, unit_prices, quantity, product_infor, categorys) # 테이블에 들어갈 것들

# 사용할 함수(메서드)
def item_append():
    item_names.append(input("제품 이름 : "))
    unit_prices.append(int(input("단가 : ")))
    quantity.append(int(input("수량 : ")))
    product_infor.append(input("상품 정보 : "))

def new_item() :
    print("new_item() 함수 호출 완료")
    print("새상품 추가용 함수로 진입합니다.")
    subRun = True
    while subRun :
        select = input("추가 하실 메뉴 카테고리 선택( ´●◡●`*) : ")
        if select == "1":
            categorys.append("교재")
        elif select == "2":
            categorys.append("잡화")
        elif select == "3":
            categorys.append("음식")
        elif select == "4":
            categorys.append("패션")
        elif select == "9":
            break
        else:
            print("다시 입력")
        item_append()
        item_add_menu()

    # 새 상품 추가용 실행문....

def item_list() :
    print("item_list() 함수 호출 완료")
    print("현재 판매중인 상품 리스트 입니다.")
    for i in range(len(item_names)) :
        print(f"{i}. {item_names[i]}")
    # 리스트 출력용 for item in item_range:

def item_view() :
    print("item_view() 함수 호출 완료")
    print("상품 자세히 보기")
    # for i in range(len(item_names)) :
    # print(f"{i}. {item_names[i]:<10}\t{unit_prices[i]:,}원\t{quantity[i]:<10}\t{product_infor[i]:<10}\t{categorys[i]:<10}")

    print(tabulate(items, headers, tablefmt="grid"))
    # 상품에 대한 상세 정보 표시

def item_update() :
    print("item_update() 함수 호출 완료")
    print("상품 수정 하기")
    item_select = int(input("수정할 상품의 번호( ´●◡●`*) : "))
    print(f"{item_select}. {item_names[item_select]} | {unit_prices[item_select]}원 | {quantity[item_select]} | {product_infor[item_select]} | {categorys[item_select]}")

    item_names[item_select] = input("이름 : ")
    unit_prices[item_select] = int(input("단가 : "))
    quantity[item_select] = int(input("수량 : "))
    product_infor[item_select] = input("설명 : ")
    categorys[item_select] = input("카테고리 : ")

    print("수정완료")
    # 상품에 대한 내용 수정하기

def item_delete() :
    print("item_delete() 함수 호출 완료")
    print("상품 삭제 하기")
    delete_select = int(input("삭제할 상품의 번호( ´●◡●`*) : "))
    print(f"{delete_select}. {item_names[delete_select]} | {unit_prices[delete_select]}원 | {quantity[delete_select]} | {product_infor[delete_select]} | {categorys[delete_select]}")
    y_no = input("삭제하시려면 y : ")
    if y_no == "y" :
        item_names.pop(delete_select)
        unit_prices.pop(delete_select)
        quantity.pop(delete_select)
        product_infor.pop(delete_select)
        categorys.pop(delete_select)
        print("삭제완료")
    else:
        print("다시 한번 확인해주세요")
    # 상품 품절, 삭제하기

def main_menu() :
    print("""
===========================
엠비시 아카데미 쇼핑몰 입니다.

1. 상품등록
2. 상품리스트
3. 상품자세히보기
4. 상품수정하기
5. 상품삭제하기

9. 프로그램 종료
""")

def item_add_menu() :
    print("""
==== 상품 추가용 메뉴에 진입 ====
1. 교재
2. 잡화
3. 음식
4. 패션

9. 종료
""")

# 프로그램 주실행 코드 시작
while run :
    main_menu() # 메인메뉴 함수 호출하여 출력

    select = input("숫자 입력( ´●◡●`*) : ")
    if select == "1" :
        item_add_menu() # 아이템 추가용 메뉴 함수
        new_item() # 아이템 추가용 코드

    elif select == "2" :
        item_list()

    elif select == "3" :
        item_view()

    elif select == "4" :
        item_update()

    elif select == "5" :
        item_delete()

    elif select == "9" :
        run = False
    else:
        print("잘못된 숫자를 입력하셨습니다.")
        print("다시 입력하세요")