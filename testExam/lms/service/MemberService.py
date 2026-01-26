from testExam.lms.domain import Member
from testExam.lms.common import Session
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..","data","members.txt")

class MemberService:
    members = []

    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for line in cls.members:
                f.write(Member.to_line(line))


    @classmethod
    def member_load(cls):
        cls.members = []
        if not os.path.exists(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH, "r",encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))



    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("ID : ")
        for member in cls.members:
            if member.uid == uid:
                print("이미 존재하는 아이디입니다.")
                return
        pw = input("Password : ")
        name = input("Name : ")
        cls.members.append(Member(uid, pw, name))
        cls.save()
        print("회원가입 완료")
        return

    @classmethod
    def login(cls):
        if Session.is_login():
            print(f"{Session.login_member.name}님 이미 로그인중")
            return
        print("\n[로그인]")
        uid = input("ID : ")
        pw = input("Password : ")
        for member in cls.members:
            if not member.is_active():
                print("비활성화 계정입니다.")
                return
            if member.uid == uid and member.pw == pw:
                Session.login(member)
                print(f"{Session.login_member.name}님({Session.login_member.role}) 환영합니다")
                print("""
.  /\_/\     (\ __ /)     A__A
\ ( ˶•ᵕ•˶)人( •ᗜ• )人(•ﻌ •  ) /
ଘ (      )  (      )｡ (      )੭
""")
                return
        print("회원정보가 일치하지 않습니다.")

    @classmethod
    def logout(cls):
        if Session.is_login():
            print(f"{Session.login_member.name}님 로그아웃 완료!!!")
            print(""". /) /)
( ･`ω´･)╮−−＝＝≡≡≡ ♡♡♡.
""")
            Session.logout()
            return
        print("로그인 후 이용해주세요")


    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요")
            return
        print("""
. ﾍ⌒ヽﾌ
（　・ω・）  [내정보 수정]
/ ~つと）
        """)
        print(f"아이디 : {Session.login_member.uid:5}")
        print(f"이름 : {Session.login_member.name:5}")
        print(f"권한 : {Session.login_member.role:7}")
        active = "활성" if Session.login_member.active else "비활성"
        print(f"활성화 : {active:5}")
        choice = input("\n1. id 2. pw 3. name 4.cancel\n")
        if choice == "1":
            uid_up = input("ID : ")
            for member in cls.members:
                if member.uid == uid_up:
                    print("이미 존재하는 아이디입니다.")
                    return
            Session.login_member.uid = uid_up
        elif choice == "2":
            Session.login_member.pw = input("pw : ")

        elif choice == "3":
            Session.login_member.name = input("Name : ")
        else:
            print("변경 취소")
            return
        cls.save()
        print("변경 완료")

    @classmethod
    def admin(cls):
        if Session.is_admin():
            while True:
                cls.admin_menu()
                choice = input(">>> : ")
                if choice == "1":
                    cls.show_list()
                elif choice == "2":
                    cls.admin_modify()
                elif choice == "3":
                    cls.admin_delete()
                else:
                    print("돌아가기")
                    return
        print("관리자만 이용 가능합니다.")

    @classmethod
    def admin_menu(cls):
        print("""
        
ᕱ⑅ᕱ
(¬`‸´¬)         관리자 메뉴  
/      / +=={:::::::::::::::::>

1. 회원조회
2. 회원정보변경
3. 회원삭제
9. 돌아가기
""")

    @classmethod
    def show_list(cls):
        for member in cls.members:
            active = "활성" if member.active else "비활성"
            print(f"ID : {member.uid:5} NAME : {member.name:5} ROLE : {member.role:7} ACTIVE : {active:5}")

    @classmethod
    def admin_modify(cls):
        sel_id = input("변경할 회원의 아이디 : ")
        for m in cls.members:
            if m.uid == sel_id:
                print("1.id 2.pw 3.name 4.role 5.active")
                admin_sel = input(">>> : ")
                if admin_sel == "1":
                    m.id = input("change id : ")
                elif admin_sel == "2":
                    m.pw = input("change pw : ")
                elif admin_sel == "3":
                    m.name = input("change name : ")
                elif admin_sel == "4":
                    if m.role == "admin":
                        print("관리자는 변경 불가")
                        return
                    sel_role = input("1.manager 2.user\n")
                    m.role = "user"
                    if sel_role == "1":
                        m.role = "manager"
                elif admin_sel == "5":
                    if m.role == "admin":
                        print("관리자는 변경 불가")
                        return
                    m.active = False if m.active else True
                else:
                    print("잘못입력하셨습니다.")
                    return
                cls.save()
                print("변경완료")
                return
        print("회원정보가 일치하지 않습니다.")

    @classmethod
    def admin_delete(cls):
        sel_id = input("삭제할 회원의 아이디 : ")
        for m in cls.members:
            if m.uid == sel_id:
                if m.role == "admin":
                    print("관리자는 삭제 불가")
                    return
                cls.members.remove(m)
                print("삭제완료")
                cls.save()
                return
        print("회원정보가 일치하지 않습니다.")