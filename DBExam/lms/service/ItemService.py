from LMS.domain.Item import Item
from LMS.common import Session
class ItemService:
    @classmethod
    def item_menu(cls):
        print("""
 ᥥ    ᥥ
(𓏸︎︎︎︎︲⤙︲𓏸︎︎︎︎) LMS 상품몰 🎀･+｡
︶∪︶︶∪︶︶︶︶︶︶︶
1. 상품목록
2. 상품담기
3. 상품구매
4. 상품취소
0. 돌아가기
        """)
    @classmethod
    def run(cls):
        while True:
            cls.item_menu()
            select = input(">>> ")
            if select == "1":
                cls.item_list()
            elif select == "2":
                cls.item_cart()
            elif select == "3":
                cls.item_buy()
            elif select == "4":
                cls.item_cancel()
            elif select == "0":
                break
            else:
                print("다시 입력")

    @classmethod
    def item_list(cls):
        print(f"{'상품명 ':<8} | {'가격 ':^10} | {'수량 ':^3}")

    @classmethod
    def item_cart(cls):
        pass

    @classmethod
    def item_buy(cls):
        pass

    @classmethod
    def item_cancel(cls):
        pass