# while 문 : run, subRun
# if문 : 메뉴 선택이나, 판단용
# for문 : 리스트에 있는 전체내용 출력용
# for in : 리스트에 있는 내용 인덱스 찾는 용

# "커피 자판기" 를 만들어 보자
# 죄송;;;;


# 커피 종류 (메인) 어서오세요 mbc커피점에
# 커피 선택
# 장바구니에 담아지기
# 결제하기
# 돈 입력받기 (카드, 현금)
# 계산해서 자판기 내부 커피 출력과 손님에게 커피 출력 그리고 거스름돈 출력

# 재고 없으면 품절


# 영수증 느낌으로 딕셔너리 1~ 점점 높여가기 첫번째 주문은 1번에 대한 메뉴 담아서 출력



stock = {"아메리카노" : 2, "카페라떼" : 3, "밀크커피" : 3, "망고쥬스" : 3, "에스프레소" : 3} # 재고용 변수
# 아메리카노 하나 주문하면 -1 뒤에 숫자가 장바구니 담기면 +1씩 업인데 이건 좀 고민중 장바구니 리스트를 하나 새로?
i =1
list = {i :[0,0,0,0,0]} # 장바구니용 변수

#리스트 변수에 담긴 상품들 갯수를 stock재고에서 빼서 다시 stock에 집어넣기

# 메뉴
mainMemu = """
=====================
어서오세요 MBC커피입니다.

1. 아메리카노 (1,500원)
2. 카페라떼 (2,000원)
3. 밀크커피 (2,000원)
4. 망고쥬스 (2,500원)
5. 에스프레소 (1,000원)


0. 계산하기

"""
a=b=c=d=e=0 # 초기 장바구니 숫자
run = True # 주 실행문용
select = None # 인풋
# i = 1 # 딕셔너리 계산용(영수증용)
card = 7000 # 카드용 사람마다 다르기에 임의로 넣음
cash = None # 현금용


# 주 실행문
while run :
    print(mainMemu)
    select = input("주문하실 메뉴를 선택해주세요 : ")
    # 아메리카노
    if select == "1" :
        # 아메리카노 현재 재고 0 방지코드
        if stock["아메리카노"] != 0:
            print("아메리카노 하나를 담으셨습니다.")
            # 재고는 있는데 현재 재고보다 많은 수량 주문시 방지코드
            if a >= stock["아메리카노"] :
                print("더 이상은 재고가 없어 주문이 불가능")
            else :
                a += 1
                list = {i : [a,b,c,d,e]}
        else:
            print("품절입니다.")
            continue
        print(list)
    # 카페라떼
    elif select == "2" :
        if stock["카페라떼"] != 0:
            print("카페라떼 하나를 담으셨습니다.")
            if a >= stock["카페라떼"]:
                print("더 이상은 재고가 없어 주문이 불가능")
            else:
                b += 1
                list = {i: [a, b, c, d, e]}
        else:
            print("품절입니다.")
            continue

    # 밀크커피
    elif select == "3" :
        if stock["밀크커피"] != 0:
            print("밀크커피 하나를 담으셨습니다.")
            if a >= stock["밀크커피"]:
                print("더 이상은 재고가 없어 주문이 불가능")
            else:
                c += 1
                list = {i: [a, b, c, d, e]}
        else:
            print("품절입니다.")
            continue

    # 망고쥬스
    elif select == "4" :
        if stock["망고쥬스"] != 0:
            print("망고쥬스 하나를 담으셨습니다.")
            if a >= stock["망고쥬스"]:
                print("더 이상은 재고가 없어 주문이 불가능")
            else:
                d += 1
                list = {i: [a, b, c, d, e]}
        else:
            print("품절입니다.")
            continue

    # 에스프레소
    elif select == "5" :
        if stock["에스프레소"] != 0:
            print("에스프레소 하나를 담으셨습니다.")
            if a >= stock["에스프레소"]:
                print("더 이상은 재고가 없어 주문이 불가능")
            else:
                e += 1
                list = {i: [a, b, c, d, e]}
        else:
            print("품절입니다.")
            continue

    # 계산하기
    elif select == "0" :
        # 가격계산
        ame = list[i][0] * 1500
        caf = list[i][1] * 2000
        mil = list[i][2] * 2000
        juc = list[i][3] * 2500
        asp = list[i][4] * 1000
        total = ame + caf + mil + juc + asp
        if total == 0 :
            print("상품을 담아주세요")
            continue
        # 프린트 장바구니 내역 0인것들은 안보이게 근데 너무 긴데 좋은 방법은 없을까
        # 현재 장바구니 내역
        if list[i][0] != 0:
            print(f"아메리카노 {a}개 {ame}원")
        if list[i][1] != 0:
            print(f"카페라떼 {b}개 {caf}원")
        if list[i][2] != 0:
            print(f"밀크커피 {c}개 {mil}원")
        if list[i][3] != 0:
            print(f"망고쥬스 {d}개 {juc}원")
        if list[i][4] != 0:
            print(f"에스프레소 {e}개 {asp}원")
        print(f"총 {total}원 입니다.")

        # 카드계산
        select = input("카드계산과 현금 계산을 선택하세요 (1~2) : ")
        if select == "1":
            if total > card:
                print("잔액이 모자릅니다.")
                continue
            else:  # total < card
                print("계산됐습니다.")
                card = card - total
                print(f"잔액이 {card}원 남았습니다.")
                stock["아메리카노"] -= a
                stock["카페라떼"] -= b
                stock["밀크커피"] -= c
                stock["망고쥬스"] -= d
                stock["에스프레소"] -= e

                a = b = c = d = e = 0  # 장바구니 초기화
                i = i + 1  # 영수증 숫자 증가

        # 현금계산
        elif select == "2":
            cash = input("현금 계산을 선택하셨습니다\n현금을 넣어주세요 : ")
            if cash.isdigit():
                cash = int(cash)
                if total > cash:
                    print("잔액이 모자릅니다.")
                    cash = None
                    continue
                else:  # total < cash
                    print("계산됐습니다.")
                    cash = cash - total
                    print(f"거스름돈 :  {cash}원")
                    stock["아메리카노"] -= a
                    stock["카페라떼"] -= b
                    stock["밀크커피"] -= c
                    stock["망고쥬스"] -= d
                    stock["에스프레소"] -= e
                    print(stock)
                    a = b = c = d = e = 0  # 장바구니 초기화
                    i = i + 1  # 영수증 숫자 증가
            else:
                print("현금을 넣어주세요")
        else:
            print("다시선택하세요")



    # 고객은 모르는 커맨드
    # 재고 조회
    elif select == "1111" :
        print(f"현재 재고\n아메리카노 : {stock['아메리카노']} 카페라떼 : {stock['카페라떼']} 밀크커피 : {stock['밀크커피']}"
              f" 망고쥬스 : {stock['망고쥬스']} 에스프레소 : {stock['에스프레소']}")

    # 재고 추가
    elif select == "2222" :
        stock['아메리카노'] += int(input("아메 추가 : "))
        stock['카페라떼'] += int(input("라떼 추가 : "))
        stock['밀크커피'] += int(input("밀크 추가 : "))
        stock['망고쥬스'] += int(input("망고 추가 : "))
        stock['에스프레소'] += int(input("에스프 추가 : "))
    else:
        print("메뉴를 선택해주세요")