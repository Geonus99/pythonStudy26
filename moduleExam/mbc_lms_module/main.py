# 주실행 코드로 주메뉴를 담당한다.
# 외부 모듈을 호출해서 연동한다.
import MemberService # 회원관리용 클래스
import ScoreService # 학생점수관리용 클래스
import BoardService # 게시판관리용 클래스
import ItemService # 상품관리용 클래스
import CartService


def main():
    boardService = BoardService.BoardService()
    scoreService = ScoreService.ScoreService()
    memberService = MemberService.MemberService()
    itemService = ItemService.ItemService()
    cartService = CartService.CartService()

    run = True
    while run:
        print(f'''
====================================
 엠비씨 아카데미 LMS 서비스 입니다.
1. 회원관리
2. 성적관리
3. 게시판
4. 상품관리
5. 장바구니

9. 종료''')
        select = input('>>> ')
        if select == '1':
            memberService.run()
        elif select == '2':
            scoreService.run()
        elif select == '3':
            boardService.run()
        elif select == '4':
            itemService.run()
        elif select == '5':
            cartService.run()
        elif select == '9':
            print('엠비씨 lms 서비스를 종료합니다.')
            run = False
        else:
            print('잘못된 번호를 선택하셨습니다.')
            print('다시 입력하세요')

if __name__ == '__main__':
    # 여러파일을 호출하기 때문에 main일때만 main()메서드를 실행
    main() # 위에 만든 main()함수를 실행한다.