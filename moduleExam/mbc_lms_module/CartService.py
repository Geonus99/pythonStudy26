class CartService:
    def __init__(self):
        self.stocks = {"두쫀쿠" : 10, "딸기시루" : 7,  "커피" : 5, "코코아" : 4, "종합영양제" : 3}
        self.i = 1 # 나중에 회원이랑 연동되면 바꿔봐
        self.carts = {self.i:[0,0,0,0,0]}
        self.card = 100000
        self.cash = None
        self.cart_mapping = {"두쫀쿠":0, '딸기시루': 1, '커피': 2, '코코아': 3, '종합영양제': 4}
        self.price = {"두쫀쿠":7000,"딸기시루":43000,"커피":3000,"코코아":1500,"종합영양제":5000}


    # 뭐뭐있는지 자동화 하고 싶어서 만들어뒀는데 아직 못씀 밑에 수동메뉴 쓰는중;;
    def stocks_ren(self):
        for idx, stock in enumerate(self.stocks.keys()):
            print(f"{idx}. {stock}")



    def cart_up(self, name):
        if self.stocks[name] != 0:
            if self.stocks[name] <= self.carts[self.i][self.cart_mapping[name]]:
                print("더 이상은 재고 부족")
                print(f"{name} 하나!")
                return
            self.carts[self.i][self.cart_mapping[name]] += 1
            print(self.carts)
        else:
            print("품절임다~~")
            return

    def stock_sub(self):
        self.stocks["두쫀쿠"] -= self.carts[self.i][0]
        self.stocks["딸기시루"] -= self.carts[self.i][1]
        self.stocks["커피"] -= self.carts[self.i][2]
        self.stocks["코코아"] -= self.carts[self.i][3]
        self.stocks["종합영양제"] -= self.carts[self.i][4]
        self.carts[self.i] = [0, 0, 0, 0, 0]


    # 메뉴
    def cart_menu(self):
        print("""
1. 두쫀쿠 (7,000)
2. 딸기시루 (43,000)
3. 커피 (3,000)
4. 코코아 (1,500)
5. 종합 영양제 (5,000)
""")

    # 1. 장바구니 물품 리스트
    # 1,2번밖에안됨 시간되면 함수로 해보셈 나머진 중복이여서
    def cart_list(self):
        buy_run = True
        while buy_run:
            self.cart_menu()
            cart_sel = input("담으실 물품 선택 : ")
            if cart_sel == "1":
                self.cart_up("두쫀쿠")

            elif cart_sel == "2":
                self.cart_up("딸기시루")

            elif cart_sel == "3":
                self.cart_up("커피")

            elif cart_sel == "4":
                self.cart_up("코코아")

            elif cart_sel == "5":
                self.cart_up("종합 영양제")

            else:
                print("끝")
                buy_run = False

    # 2. 장바구니 담은거 보기
    def cart_see(self):
        print(f"{self.i}님")
        if self.carts[self.i][0] != 0:
            print(f"두쫀쿠 : {self.carts[self.i][0]}개")
        if self.carts[self.i][1] != 0:
            print(f"딸기시루 : {self.carts[self.i][1]}개")
        if self.carts[self.i][2] != 0:
            print(f"커피 : {self.carts[self.i][2]}개")
        if self.carts[self.i][3] != 0:
            print(f"코코아 : {self.carts[self.i][3]}개")
        if self.carts[self.i][4] != 0:
            print(f"종합영양제 : {self.carts[self.i][4]}개")


    # 3. 장바구니 구매하기
    def cart_buy(self):
        du = self.carts[self.i][0] * 7000
        stv = self.carts[self.i][1] * 43000
        cof = self.carts[self.i][2] * 3000
        coc = self.carts[self.i][3] * 1500
        vit = self.carts[self.i][4] * 5000
        total = du + stv + cof + coc + vit
        if total == 0 :
            print("상품을 담아주세요")
            return
        self.cart_see()
        print(f"총 : {total:,}원 입니다.")
        buy_sel = input("1.현금 2.카드")
        if buy_sel == "1":
            money = int(input("현금 : "))
            if total > money :
                print("잔액이 부족합니다.")
                return
            money = money - total
            print("계산됐습니다")
            print(f"거스름돈 : {money:,}이요 또 오세요")
            self.stock_sub()
            print(self.stocks)
        elif buy_sel == "2":
            if self.card > total:
                self.card = self.card - total
                print("계산됐습니다")
                print(f"남은 잔액 : {self.card:,}")
                self.stock_sub()
            else:
                print("잔액이 모자릅니다.")


    # 4. 장바구니 취소하기
    def cart_cancel(self):
        self.carts[self.i] = [0,0,0,0,0]
        print("장바구니 초기화~~")

    # 실행문
    def run(self):
        subrun = True
        while subrun:
            print("""
-------------------------
1. 장바구니 물품 리스트
2. 장바구니 담은거 보기
3. 장바구니 구매하기
4. 장바구니 취소하기

9. 장바구니 서비스 종료
""")
            subselect = input(">>> ")
            if subselect == "1":
                self.cart_list()

            elif subselect == "2":
                print("장바구니 담은거 보기")
                self.cart_see()

            elif subselect == "3":
                print("장바구니 구매하기")
                self.cart_buy()

            elif subselect == "4":
                print("장바구니 취소하기")
                self.cart_cancel()

            elif subselect == "1111":
                print("현재재고")
                print(self.stocks)

            elif subselect == "2222":
                self.stocks['두쫀쿠'] += int(input("두쫀쿠 추가 : "))
                self.stocks['딸기시루'] += int(input("딸기시루 추가 : "))
                self.stocks['커피'] += int(input("커피 추가 : "))
                self.stocks['코코아'] += int(input("코코아 추가 : "))
                self.stocks['종합영양제'] += int(input("종합영양제 추가 : "))

            elif subselect == "9":
                subrun = False

            else:
                print("잘못입력하셨습니다.\n다시 선택하세요")
