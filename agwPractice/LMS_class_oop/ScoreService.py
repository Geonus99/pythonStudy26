from Score import Score
import os

import MemberService
import Member
MemberService = MemberService.MemberService()

class ScoreService:
    def __init__(self,file_name = "scores.txt",):
        self.file_name = file_name
        self.scores = []
        self.session = MemberService.session_maintain()
        self.load_scores()





    def load_scores(self):
        if not os.path.exists(self.file_name):
            self.save_scores()
            return

        self.scores = []
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                self.scores.append(Score.from_line(line))

    def save_scores(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for score in self.scores:
                f.write(score.to_line())

    def score_add(self):
        uid = input("id : ")
        py = int(input("py : "))

    def score_list(self):
        print(self.scores)
    def score_modify(self):
        pass


    def score_menu(self):
        print("""
==== 성적관리 프로그램 (Member 객체 기반) ====
1. 로그인
2. 로그아웃
3. 성적보기
4. 성적입력
5. 성적수정
9. 종료
""")

    def run(self):
        run = True
        while run:
            self.score_menu()
            sel = input(">>> ")
            if sel == "1":
                print(MemberService.session)
                MemberService.member_login()
            elif sel == "2":
                MemberService.member_logout()
            elif sel == "3":
                self.score_list()
            elif sel == "4":
                self.score_add()
            elif sel == "5":
                self.score_modify()
            elif sel == "9":
                run = False
            else:
                print("잘못입력하셨습니다.")


