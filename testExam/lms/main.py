from testExam.lms.common import Session
from testExam.lms.service import *

import os

def main():
    MemberService.member_load()

    run = True
    while run:
        print("""\033[35m
.⠀∧,,,∧   ~ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
(  ̳• · • ̳)   ~ 🎀 MBC 아카데미 관리 시스템 🎀
/       づ ~┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
\033[97m
1. 회원가입  2. 로그인 3. 로그아웃
4. 내정보수정 5. 관리자메뉴  
9. 종료
""")

        if not Session.is_login():
            print("\033[35m ＾  　0o0")
            print("\033[35mミ ・ 。・ ミ   비로그인! \033[97m")
            print("————○———○————————————————")
        else:
            print("\033[35m ＾  　0o0")
            print(f"\033[35mミ ・ 。・ ミ    {Session.login_member.name}님\033[97m")
            print("————○———○————————————————")

        sel = input(">>> ")
        if sel == "1":
            MemberService.signup()
        elif sel == "2":
            MemberService.login()
        elif sel == "3":
            MemberService.logout()
        elif sel == "4":
            MemberService.modify()
        elif sel == "5":
            MemberService.admin()
        elif sel == "9":
            print("프로그램 종료")
            run = False
        else:
            print("메뉴를 선택하세요")
if __name__ == "__main__":
    main()