from lms.service import *
from lms.common.Session import Session
def main():
    MemberService.load()

    run = True
    while run:
        print("""\033[35m
    .⠀∧,,,∧   ~ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    (  ̳• · • ̳)   ~ 🎀 MBC 아카데미 관리 시스템 🎀
    /       づ ~┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    \033[97m
    1. 회원가입  2. 로그인 3. 로그아웃
    4. 내정보수정 5. 게시판 6. 성적
    7. 관리자메뉴  
    9. 종료
    """)
        member = Session.login_member
        if member is None:
            print("현재 로그인 상태가 아닙니다.")
        else:
            print(f"{member.name}님 환연합니다.")

        sel = input("선택 : ")
        if sel == "1":
            print("\n[회원가입]")
            MemberService.signup()
        elif sel == "2":
            print("\n[로그인]")
            MemberService.login()
        elif sel == "3":
            print("\n[로그아웃]")
            MemberService.logout()
        elif sel == "4":
            print("\n[회원수정]")
            MemberService.modify()
        elif sel == "5":
            pass
        elif sel == "6":
            pass
        elif sel == "7":
            MemberService.admin()
        elif sel == "9":
            run = False
        else:
            print("잘못입력하셨습니다.")

if __name__ == "__main__":
    main()