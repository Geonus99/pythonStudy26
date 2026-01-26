import os

# 회원가입으로 관리자,매니져를 생성 못하기에
# kkw|1111|김기원|admin|True
# 메모장에 추가해두고 써야함

class MemberManager:
    def __init__(self, file_name="members.txt",file_name_score="scores.txt"):
        self.file_name = file_name
        self.members = []
        self.session = None
        self.load_member()

        self.file_name_score = file_name_score
        self.scores = []
        self.load_score()




    # 회원찾기용
    def search_member(self):
        uid = input("찾는 회원 id : ")
        for m in self.members:
            if m[0] == uid:
                return m
        print("존재하지 않음")
        return

    # 성적찾기용
    def search_score(self):
        uid = input("찾는 회원 id : ")
        for s in self.scores:
            if s[0] == uid:
                return s
        print("존재하지 않음")
        return



    # 파일로드
    def load_member(self):
        if not os.path.exists(self.file_name):
            self.save_member()
            return

        with open(self.file_name, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("|")
                data[4] = True if data[4] == "True" else False
                self.members.append(data)

    def load_score(self):
        if not os.path.exists(self.file_name_score):
            self.save_score()
            return

        with open(self.file_name_score, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("|")
                self.scores.append(data)


    # 파일저장
    def save_member(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            for m in self.members:
                file.write(f"{m[0]}|{m[1]}|{m[2]}|{m[3]}|{m[4]}\n")

    def save_score(self):
        with open(self.file_name_score, "w", encoding="utf-8") as file:
            for s in self.scores:
                file.write(f"{s[0]}|{s[1]}|{s[2]}|{s[3]}|{s[4]}|{s[5]}\n")


    # 회원가입
    def member_add(self):
        uid = input("id : ")
        for m in self.members:
            if m[0] == uid:
                print("이미 존재하는 아이디")
                return

        pw = input("pw : ")
        name = input("name : ")

        # print("1.admin  2.manager  3.user")
        # sel = input("(1~3) : ")
        rule = "user"
        # if sel == "1":
        #     rule = "admin"
        # elif sel == "2":
        #     rule = "manager"
        active = True

        print(f"id : {uid} pw : {pw} name : {name} rule : {rule} active : {active}")
        sure = input("맞으면 y : ")
        if sure == "y":
            self.members.append([uid, pw, name, rule, active])
            self.save_member()
            print("가입 완료")
            return
        else:
            print("가입 취소")
            return

    # 로그인
    def member_login(self):
        if not self.session is None:
            print(f"{self.members[self.session][0]}님 이미 로그인중")
            return

        uid = input("id : ")
        for idx, m in enumerate(self.members):
            if m[0] == uid:
                pw = input("pw : ")
                if m[1] == pw:
                    self.session = idx
                    print(f"{m[2]}님 로그인완료")
                    return
                print("비밀번호가 맞지 않음")
                return
        print("아이디가 존재하지 않음")
        return

    # 로그아웃
    def member_logout(self):
        if self.session is None:
            print("로그인후 이용해주세요")
            return

        self.session = None
        print("로그아웃 완료")
        return

    # 회원수정
    def member_modify(self):
        if self.session is None:
            print("로그인후 이용해주세요")
            return
        print("1.아이디수정 2.비밀번호수정 3.이름수정 4.권한변경 5.상태변경")
        print("취소를 원하시면 엔터")
        sel = input("(1~5) : ")

        # 아이디변경
        if sel == "1":
            if self.members[self.session][3] == "admin" or self.members[self.session][3]== "manager":
                mem_list = self.search_member()
                if mem_list is None:
                    return
                mem_list[0] = input("id : ")
                self.save_member()
                print("수정완료")
                return
            self.members[self.session][0] = input("id : ")
            self.save_members()
            print("수정완료")
            return

        # 비번변경
        elif sel == "2":
            if self.members[self.session][3] == "admin" or self.members[self.session][3] == "manager":
                mem_list = self.search_member()
                if mem_list is None:
                    return
                mem_list[1] = input("pw : ")
                self.save_member()
                print("수정완료")
                return
            self.members[self.session][1] = input("pw : ")
            self.save_members()
            print("수정완료")
            return

        # 이름변경
        elif sel == "3":
            if self.members[self.session][3] == "admin" or self.members[self.session][3] == "manager":
                mem_list = self.search_member()
                if mem_list is None:
                    return
                mem_list[2] = input("name : ")
                self.save_member()
                print("수정완료")
                return
            self.members[self.session][2] = input("name : ")
            self.save_members()
            print("수정완료")
            return

        # 권한변경
        elif sel == "4":
            if self.members[self.session][3]== "admin":
                for i in self.members:
                    print(f"{i}\n")
                sel = input("권한 변경할 회원의 아이디 : ")
                for m in self.members: # 아이디 유무 찾는거좀 중복되는데 함수로 빼볼래?
                    if m[0] == sel:
                        if m[3]== "admin":
                            print("관리자는 변경 불가능")
                            return
                        print("1.admin  2.manager  3.user")
                        r = input("권한 선택 : ")

                        role = "user"
                        if r == "1":
                            role = "admin"
                        elif r == "2":
                            role = "manager"
                        m[3] = role
                        self.save_member()
                        print("변경 완료")
                        return
            print("관리자만 이용 가능")
            return

        # 블랙리스트변경
        elif sel == "5":
            if self.members[self.session][3]== "admin" or self.members[self.session][3]== "manager":
                for i in self.members:
                    print(f"{i}\n")
                sel = input("상태 바꿀 회원의 아이디 : ")
                for m in self.members:
                    if m[0] == sel:
                        if m[3]== "admin":
                            print("관리자는 불가능")
                            return
                        print("1.True 2.False")
                        sel = input("(1~2) : ")
                        if sel == "2":
                            m[4] = False
                            print("변경 완료")
                            self.save_member()
                            return
                        m[4] = True
                        print("변경 완료")
                        self.save_member()
                        return
            print("관리자나 매니져만 이용 가능")
            return


        else:
            print("수정 취소")
            return

    # 회원탈퇴
    def member_delete(self):
        if self.session is None:
            print("로그인후 이용해주세요")
            return

        if self.members[self.session][3] == "admin" or self.members[self.session][3] == "manager":
            mem_list = self.search_member()
            if mem_list is None:
                print("찾는 회원이 없습니다.")
                return
            del_sel = input("탈퇴시키려면 y"
                            "아니라면 아무거나 눌러주세요 : ")
            if del_sel == "y":
                for idx, m in enumerate(self.members) :
                    if m[0] == mem_list[0]:
                        self.members.pop(idx)
                        print("탈퇴 완료")
                        self.save_member()
                        return
            print("탈퇴 취소")
            return

        del_sel = input("탈퇴하시려면 y"
                        "아니라면 아무거나 눌러주세요 : ")
        if del_sel == "y":
            self.members.pop(self.session)
            self.session = None
            self.save_member()
            print("탈퇴완료")
            return
        print("탈퇴취소")
        return


    # 성적입력
    def score_add(self):
        if self.members[self.session][3] == "admin" or self.members[self.session][3] == "manager":
            stu = self.search_member()
            if stu is None:
                print("찾는 학생이 없어요")
                return

            if stu[3] == "user" :
                py = int(input("py : "))
                db = int(input("db : "))
                web = int(input("web : "))
                # 0~100 검사하는거 나중에 추가
                total = py + db + web
                avg = total / 3
                if avg >= 90 :
                    grade = "A"
                elif avg >= 80 :
                    grade = "B"
                else:
                    grade = "F"
                self.scores.append([stu[0],py, db, web, total, grade])
                self.save_score()
                print("입력완료")
                return

            print("학생 성적만 입력가능합니다")
            return

        print("학생은 못해용")
        return

    # 성적삭제
    def score_delete(self): # 회원삭제랑 중복되는데 함수 쓰면 좋을거 같음
        if self.members[self.session][3] == "admin" or self.members[self.session][3] == "manager":
            stu_list = self.search_score()
            if stu_list is None:
                return
            del_sel = input("삭제시키려면 y"
                            "아니라면 아무거나 눌러주세요 : ")
            if del_sel == "y":
                for idx, m in enumerate(self.scores):
                    if m is None :
                        print("성적이 존재하지 않습니다.")
                        return
                    if m[0] == stu_list[0]:
                        self.scores.pop(idx)
                        print("삭제 완료")
                        self.save_score()
                        return
            print("삭제 취소")
            return

        print("학생은 못해용")
        return

    # 성적보기
    def score_see(self):
        if self.members[self.session][3] == "user" :
            for s in self.scores :
                if self.members[self.session][0] == s[0]:
                    print(f"{s[0]}님의 성적\n"
                          f"py : {s[1]} db : {s[2]} web : {s[3]} grade : {s[5]}")
                    return
        print(self.scores) # 걍 다뿌리게 해둠 나중에 꾸미자..
        return

    # 성적수정
    def score_modify(self):
        if self.session is None:
            print("로그인후 이용해주세요")
            return
        if self.members[self.session][3] == "admin" or self.members[self.session][3] == "manager":
            stu_list = self.search_score()
            if stu_list is None:
                return
            print("1.Py 2.DB 3.Web")
            modi_sel = input("(1~3) : ") # 총점과 등급수정이 반영안됨 나중에 추가하셈(총점 등급 계산 함수 만들어서 하면 될듯)
            # toAvg_cal(self)
            if modi_sel == "1":
                stu_list[1] = int(input("py : "))
                self.save_score()
                print("수정완료")
                return
            elif modi_sel == "2":
                stu_list[2] = int(input("db : "))
                self.save_score()
                print("수정완료")
                return
            elif modi_sel == "3":
                stu_list[3] = int(input("web : "))
                self.save_score()
                print("수정완료")
                return
            print("취소")
            return
        print("학생은 못해용")
        return

    # 아직 못함
    # # 총점 등급 계산기
    # def toAvg_cal(self):
    #     total = self.stu_list[1]+self.stu_list[2]+self.stu_list[3]
    #     avg = total / 3
    #     if avg >= 90 :
    #         grade = "A"
    #     elif avg >= 80 :
    #         grade = "B"
    #     else:
    #         grade = "F"
    #     return

    # 메인메뉴
    def main_menu(self):
        print("""
MBC 회원관리 프로그램
1. 회원가입     2. 로그인      3. 로그아웃
4. 회원정보수정  5. 회원탈퇴    6. 성적
0. 종료
""")

    # 성적메뉴
    def score_menu(self):
        print("""
MBC 성적관리 프로그램
1.성적입력     2.성적조회      
3.성적수정     4.성적삭제
0.뒤로가기
""")


    # 회원관리 실행
    def run(self):
        while True:
            self.main_menu()
            sel = input(">>> ")

            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_modify()
            elif sel == "5": self.member_delete()
            elif sel == "6": self.score_run()
            elif sel == "0": break


    # 스코어 실행
    def score_run(self):
        if self.session is None:
            print("로그인후 이용 바랍니다")
            return
        while True:
            self.score_menu()
            sel = input(">>> ")

            if sel == "1": self.score_add()
            elif sel == "2": self.score_see()
            elif sel == "3": self.score_modify()
            elif sel == "4": self.score_delete()
            elif sel == "0": break

# 프로그램 시작
app = MemberManager()
app.run()