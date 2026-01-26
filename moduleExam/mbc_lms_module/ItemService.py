class ItemService :
    def __init__(self) :

        self.items = []
        self.prices = []
        self.quantity = []
        self.product_info = []
        self.category = []

# ----------------------------------------------------------------------------------------------------------------------

    # 사용할 매서드
    # ============
    # C : 상품 등록
    # ============
    def new_item(self) :
        print("상품 등록 메뉴에 진입하였습니다.")

        self.item_add_menu()

        cat_num = input(">>> ")

        if cat_num == "1" :
            cat = "교재"

        elif cat_num == "2" :
            cat = "잡화"

        elif cat_num == "3" :
            cat = "음식"

        elif cat_num == "4" :
            cat = "패션"

        elif cat_num == "9" :
            cat = "종료"

        else :
            print("잘못 입력하였습니다.")
            return

        name = input("상품명 : ")
        price = int(input("가격 : "))
        qty = int(input("수량 : "))
        info = input("상품 설명 : ")

        self.items.append(name)
        self.prices.append(price)
        self.quantity.append(qty)
        self.product_info.append(info)
        self.category.append(cat)

        print("상품 등록이 완료되었습니다.")

    # =============
    # R1 : 상품 목록
    # =============
    def item_list(self) :
        print("상품 목록 메뉴에 진입하였습니다.")
        print("| 번호 | 상품명 | 가격 | 수량 | 카테고리 | 상세 정보 |")

        for i in range (len(self.items)) :
            print(f"| {i + 1} | {self.items[i]} | {self.prices[i]} | {self.quantity[i]} | {self.category[i]} | {self.product_info[i]} |")

    # ===================
    # R2 : 상품 자세히 보기
    # ===================
    def item_view(self) :
        print("상품 자세히 보기 메뉴에 진입하였습니다.")
        print("| 번호 | 상품명 |")

        for i in range (len(self.items)) :
            print(f"| {i + 1} | {self.items[i]} |")

        idx = int(input("상품 번호 : "))

        if 0 < idx <= len(self.items) :
            print("상품명 : " , self.items[idx - 1])
            print("가격 : " , self.prices[idx - 1])
            print("수량 : " , self.quantity[idx - 1])
            print("카테고리 : " , self.category[idx - 1])
            print("상세 정보 : " , self.product_info[idx - 1])

        else :
            print("존재하지 않는 상품입니다.")

    # ============
    # U : 상품 수정
    # ============
    def item_update(self) :
        print("상품 수정 메뉴로 진입하였습니다.")

        self.item_list()

        idx = int(input("상품 번호 : "))

        if 0 < idx <= len(self.items) :

            self.item_update_menu()

            subchoice = input(">>> ")

            if subchoice == "1" :

                name = input(f"기존의 상품명 : {self.items[idx-1]} → ")

                print("상품명이 변경되었습니다.")

                self.items[idx - 1] = name

            elif subchoice == "2" :

                price = input(f"기존의 가격 : {self.prices[idx-1]} → ")

                print("가격이 변경되었습니다.")

                self.prices[idx - 1] = price


            elif subchoice == "3" :

                qty = int(input(f"기존의 수량 : {self.quantity[idx] - 1} → "))

                print("수량이 변경되었습니다.")

                self.quantity[idx - 1] = int(qty)

            elif subchoice == "4" :

                info = input(f"기존의 상세 정보 : {self.product_info[idx - 1]} → ")

                print("상세 정보가 변경되었습니다.")

                self.product_info[idx - 1] = info

            else :
                print("잘못 입력하였습니다.")

        else :
            print("존재하지 않는 상품입니다.")

    # ============
    # D : 상품 품절
    # ============
    def item_delete(self) :
        print("상품 품절 메뉴로 진입하였습니다.")

        self.item_list()

        idx = int(input("상품 번호 : "))

        if 0 < idx <= len(self.items) :

            self.items.pop(idx - 1)
            self.prices.pop(idx - 1)
            self.quantity.pop(idx - 1)
            self.category.pop(idx - 1)
            self.product_info.pop(idx - 1)

            print("상품의 품절 처리가 완료되었습니다.")

        else :
            print("존재하지 않는 상품입니다.")

# ----------------------------------------------------------------------------------------------------------------------

    # 사용할 메뉴
    # ==========
    # 추가용 메뉴
    # ==========
    def item_add_menu(self) :
        print("""
--------------------------------
추가할 상품의 카테고리를 선택하세요.
--------------------------------
1. 교재
2. 잡화
3. 음식
4. 패션

9. 종료
""")

    # ==========
    # 수정용 메뉴
    # ==========
    def item_update_menu(self) :
        print("""
-----------------------
수정할 항목을 선택하세요.
-----------------------
1. 상품명
2. 가격
3. 수량
4. 상세 정보
""")

# ----------------------------------------------------------------------------------------------------------------------
    # 클래스 실행 코드
    def run(self):

        subRun = True

        while subRun:
            print("""
--------------------------------
교보재 관리 서비스로 진입하였습니다.
--------------------------------
1. 상품 등록
2. 상품 목록
3. 상품 자세히 보기
4. 상품 수정
5. 상품 삭제

9. 교보재 관리 서비스 종료
""")

            subSelect = input(">>> ")

            if subSelect == "1":
                print("상품 등록 매서드를 호출합니다.")
                self.new_item()

            elif subSelect == "2":
                print("상품 목록 매서드를 호출합니다.")
                self.item_list()

            elif subSelect == "3":
                print("상품 자세히 보기 매서드를 호출합니다.")
                self.item_view()

            elif subSelect == "4":
                print("상품 수정 매서드를 호출합니다.")
                self.item_update()

            elif subSelect == "5":
                print("상품 품절 매서드를 호출합니다.")
                self.item_delete()

            elif subSelect == "9":
                print("교보재 관리 서비스를 종료합니다.")
                break

            else:
                print("잘못 입력하였습니다.")
