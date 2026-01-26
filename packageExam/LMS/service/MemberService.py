import os

from packageExam.LMS.domain import Member
from packageExam.LMS.common import Session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..","data","member.txt")
# FILE_PATH = "data/member.txt"

class MemberService:

    members = []

    @classmethod
    def load(cls):
        cls.members = []

        if not os.path.exists(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")


    @classmethod
    def login(cls):
        if Session.login_member is not None:
            print(f"{Session.login_member.name}님 로그인중")
            return
        print("\n[로그인]")
        uid = input("id : ")
        pw = input("pw : ")
        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    return
                if m.pw == pw:
                    print(f"{m.name}님 로그인 성공 {m.role}")
                    Session.login_member = Member(m.uid, m.pw, m.name, m.role)
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    return
        print("존재하지 않는 아이디입니다.")

    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("id : ")
        if any(m.uid == uid for m in cls.members):
            print("이미 존재하는 아이디입니다.")
            return
        pw = input("pw : ")
        name = input("name : ")
        member = Member(uid, pw, name)
        cls.members.append(member)
        cls.save()
        print("회원가입 완료")

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요")
            return
        Session.logout()
        print("로그아웃")

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요")
            return
        if Session.is_admin():
            cls.admin_menu()
            return
        sel = input("[회원정보 변경]\n1.비밀번호 2.이름 3.탈퇴 0.cancel\n")
        if sel == "1":
            Session.login_member.pw = input("pw : ")
        elif sel == "2":
            Session.login_member.name = input("name : ")
        elif sel == "3":
            cls.members.remove(Session.login_member)
            Session.login_member = None
        else:
            print("취소")
        print("수정 완료")
        cls.save()
        return

    @classmethod
    def admin_menu(cls):
        while True:
            print("""
[관리자 메뉴]
1. 회원 목록 조회
2. 권한 변경
3. 블랙리스트 처리
4. 회원 탈퇴
0. 뒤로가기
""")
            sel = input(">> ")
            if sel == "1":
                cls.show_list()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.black_member()
            elif sel == "4":
                cls.delete_member()
            elif sel == "0":
                break
            else:
                print("잘못 입력하셨습니다.")

    @classmethod
    def show_list(cls):
        print("\n[회원 목록]")
        for m in cls.members:
            print(m)

    @classmethod
    def change_role(cls):
        print("[권한 변경]")
        uid = input("변경할 회원 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                if m.role == "admin":
                    print("관리자는 변경 불가")
                    return
                sel = input("1.manager 2.user\n")
                m.role = "user"
                if sel == "1":
                    m.role = "manager"
                cls.save()
                print("변경완료")
                return
        print("존재하지 않는 아이디")

    @classmethod
    def black_member(cls):
        print("[블랙리스트 변경]")
        uid = input("블랙할 id : ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False if m.active else True
                cls.save()
                print("변경완료")
                return
        print("존재하지 않는 아이디")

    @classmethod
    def delete_member(cls):
        uid = input("탈퇴할 id : ")
        for m in cls.members:
            if m.uid == uid:
                cls.members.remove(m)
                print("탈퇴 완료")
                cls.save()
                return
        print("존재하지 않는 아이디")