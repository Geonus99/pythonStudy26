from packageExam.LMS.common import Session
from packageExam.LMS.service import *

def main():
    MemberService.load()
    run = True
    while run:
        print("""
==========================
 MBC 아카데미 관리 시스템
==========================
1. 회원가입  2. 로그인 3. 로그아웃
4. 회원관리 (관리자)  
5. 게시판  6. 성적관리 9. 종료
""")
        select = input(">>>\n")
        if select == "1":
            MemberService.signup()
        elif select == "2":
            MemberService.login()
        elif select == "3":
            MemberService.logout()
        elif select == "4":
            MemberService.modify()
        elif select == "5":
            BoardService.run()
        elif select == "6":
            pass
        elif select == "9":
            run = False
        else:
            print("잘못입력하셨습니다.")

if __name__ == "__main__":
    main()