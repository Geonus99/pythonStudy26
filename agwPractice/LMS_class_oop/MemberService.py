from Member import Member
import os

class MemberService:
    def __init__(self, file_name = "members.txt"):
        self.file_name = file_name
        self.session = None
        self.members = []
        self.load_members()


    def session_maintain(self):
        self.session = self.find_member(self.session)
        return self.session

    def load_members(self):
        if not os.path.exists(self.file_name):
            self.save_members()
            return

        self.members = []
        with open(self.file_name, "r",encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))

    def save_members(self):
        with open(self.file_name, "w",encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())

    def find_member(self, uid):
        for member in self.members:
            if member.id == uid:
                print(member.name,"님을 찾았습니다.")
                return member
        return None

    def main_menu(self):
        print("""
==== 회원관리 프로그램 (Member 객체 기반) ====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료
""")

    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input(">>> ")
            if sel == "1":
                self.member_add()
            elif sel == "2":
                self.member_login()
            elif sel == "3":
                self.member_logout()
            elif sel == "4":
                self.member_modify()
            elif sel == "5":
                self.member_delete()
            elif sel == "9":
                run = False
            else:
                print("잘못입력하셨습니다.")

    def member_add(self):
        print("\n[회원가입]")
        uid = input("id : ")


        if self.find_member(uid):
            print("이미 존재하는 아이디입니다")
            return

        pw = input("pw : ")
        name = input("name : ")
        role = "user"
        self.members.append(Member(uid, pw, name, role))
        self.save_members()
        print("가입 완료")

    def member_login(self):
        print("\n[로그인]")
        if self.session is not None:
            print(f"{self.session}이미 로그인중")
            return

        uid = input("id : ")
        pw = input("pw : ")
        
        member = self.find_member(uid)
        if not member :
            print("존재하지 않는 아이디.")
            return
        
        if not member.active :
            print("비활성화 계정")
            return
        
        if member.pw == pw :
            self.session = member
            print(f"{member.name}님 로그인 성공({member.role})")
            
            if member.role == "admin":
                self.member_admin()
        else:
            print("비밀번호 오류")
            


    def member_logout(self):
        if self.session is None:
            print("로그아웃상태입니다.")
            return
        # 세션에 객체가 들어가 있는 상태
        self.session = None
        print("로그아웃")

    def member_modify(self):
        print("\n[회원정보수정]")
        member = self.session
        if member.role == "admin":
            self.member_admin()
            return

        sel = input("1.아이디 2.비밀번호 3.이름")
        if sel == "1":
            member.id = input("id : ")
        elif sel == "2":
            member.pw = input("pw : ")
        elif sel == "3":
            member.name = input("name : ")
        else:
            print("잘못 입력")
        self.save_members()
        print("변경완료")

    def member_delete(self):
        print("\n[회원 삭제]")
        member = self.session
        if member.role == "admin":
            mem = self.find_member(input("대상 아이디 : "))
            if mem.role == "admin":
                print("관리자는 삭제 불가")
                return
            print(f"{mem.id:10}{mem.name:10}{mem.role:10}{mem.id}")
            sel = input("삭제하시려면 y\n")
            if sel == "y":
                self.members.remove(mem)
                self.save_members()
                return
            print("취소")
            return
        sel = input(f"{member.id}님 탙퇴하시려면 y\n")
        if sel == "y":
            self.members.remove(member)
            self.save_members()
            self.session = None
            return
        print("취소")
        return

    def member_admin(self):
        subrun = True
        while subrun:
            print("\n[관리자 메뉴]")
            print("1. 회원 리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("9. 종료")

            sel = input("선택 : ")

            if sel == "1": self.show_member_list()
            elif sel == "2":
                uid = input("대상 id : ")
                member = self.find_member(uid)
                if member :
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
                    print("비번 변경완료")
                else:
                    print("존재하지 않음")
            elif sel == "3":
                uid = input("대상 id : ")
                member = self.find_member(uid)
                if member and member.role=="admin":
                    print("관리자는 변경 불가")
                    continue
                if member :
                    member.active = False if member.active else True
                    self.save_members()
                    print("블랙 변경완료")
                else:
                    print("존재하지 않음")
            elif sel == "4":
                uid = input("대상 id : ")
                member = self.find_member(uid)
                if member and member.role=="admin":
                    print("관리자는 변경 불가")
                    continue
                if member :
                    sel = input("1.manager 2.user\n")
                    member.role = "user"
                    if sel == "1":
                        member.role = "manager"
                    self.save_members()
                    print("역할 변경완료")
            elif sel == "9":
                subrun = False
            self.save_members()

    def show_member_list(self):
        print("\n[회원 목록]")
        print("-" * 60)
        print(f"{'ID':10}{'이름':10}{'권한':10}{'상태'}")
        print("-" * 60)
        for member in self.members:
            # members 리스트에 있는 객체를 하나씩 가져와 member에 넣음
            status = "활성" if member.active else "비활성"
            # member.active == True면 status변수에 "활성" 아니면 "비활성"
            print(f"{member.id:10}{member.name:10}{member.role:10}{status}")
            #                                                  "활성" | "비활성"
        print("-" * 60)


