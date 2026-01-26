from packageExam.LMS.common import Session
from packageExam.LMS.domain import Board
import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# FILE_PATH = os.path.join(BASE_DIR, "..", "data", "board.txt")
FILE_PATH = "data/board.txt"

class BoardService:

    boards = []

    @classmethod
    def board_menu(cls):
        print("""
====================
 게시판
====================
1. 게시글 등록
2. 게시글 보기
3. 게시글 수정
4. 게시글 삭제
0. 뒤로가기
""")

    @classmethod
    def load(cls):
        if not os.path.exists(FILE_PATH):
            cls.save()
            return
        with open(FILE_PATH, "r",encoding="utf-8") as f:
            for line in f:
                cls.boards.append(Board.from_line(line))

    @classmethod
    def save(cls):
        with open(FILE_PATH, "w",encoding="utf-8") as f:
            for b in cls.boards :
                f.write(b.to_line() + "\n")

    @classmethod
    def run(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요")
            return

        cls.load()

        while True:
            cls.board_menu()
            sel = input(">>> ")
            if sel == "1":
                cls.board_up()
            elif sel == "2":
                cls.board_show()
            elif sel == "3":
                cls.board_modify()
            elif sel == "4":
                cls.board_delete()
            elif sel == "0":
                break
            else:
                print("잘못입력하셨습니다.")

    @classmethod
    def board_up(cls):
        print("\n[글 등록]")
        title = input("제목 : ")
        content = input("내용 : ")
        no = len(cls.boards)+1
        writer = Session.login_member.name
        sel = input("등록하시겠습니까?(y/n) : ")
        if sel == "y":
            cls.boards.append(Board(no, title, content, writer))
            print("등록완료")
            cls.save()
            return
        else:
            print("취소")


    @classmethod
    def board_show(cls):
        print("\n[글 목록]")
        for b in cls.boards:
            print(b)

    @classmethod
    def board_modify(cls):
        print("\n[글 수정]")
        for b in cls.boards:
            print(b)
        sel = input("수정할 글 번호 : ") # 아무나 수정가능한거 고치삼
        for b in cls.boards:
            if sel == b.no :
                print("1.제목 2.내용")
                choice = input(">> ")
                if choice == "1":
                    b.title = input("제목 : ")
                elif choice == "2":
                    b.content = input("내용 : ")
                else:
                    print("잘못입력하셨습니다.")
                cls.save()
                print("변경완료")
                return
        print("찾는 번호가 없습니다.")

    @classmethod
    def board_delete(cls):
        if Session.is_admin():
            print("\n[글 삭제]")
            for b in cls.boards:
                print(b)
            sel = input("삭제할 글 번호 : ")  # 아무나 삭제가능한거 고치삼
            for b in cls.boards:
                if sel == b.no:
                    cls.boards.remove(b)
                    cls.save()
                    print("삭제완료")
                    return
            print("취소")
            return
        print("관리자만 이용해주세요")