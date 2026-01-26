class BoardService:
    def __init__(self):
        # 데이터 : [제목, 내용, 작성자, 비번, 조회수, 좋아요]
        self.boards = []

    def show_boards(self):
        print('---------------- 게시판 목록 ------------------')
        if len(self.boards) == 0:
            print('게시판 목록이 비었습니다.')
        else:
            print(f'{"No.":10}|{"제목":10}|{"작성자":10}|{"조회수":10}|{"좋아요":10}')
            for idx, board in enumerate(self.boards):
                print(f'{idx:<10}|{board[0]:<10}|{board[2]:<10}|{board[4]:<10}|{board[5]:<10}')

    def show_board_detail(self):
        print('----------------- 게시글 상세 보기 ------------------')
        self.show_boards()
        if len(self.boards) == 0:
            print('게시글이 없습니다. 게시글을 생성해주세요.')
            return

        sel = input('>>> ')
        if sel.isdigit() and int(sel) in range(len(self.boards)):
            self.boards[int(sel)][4] += 1
            print(f'제목 : {self.boards[int(sel)][0]}')
            print(f'내용 : {self.boards[int(sel)][1]}')
            print(f'작성자 : {self.boards[int(sel)][2]}')
            print(f'조회수 : {self.boards[int(sel)][4]}')
            print(f'좋아요 : {self.boards[int(sel)][5]}')
            print('좋아요를 하시겠습니까? ')
            print('1. 좋아요')
            print('2. 뒤로가기')
            subSelect = input('>>> ')
            if subSelect == '1':
                self.boards[int(sel)][5] += 1
                print('해당 게시글에 좋아요를 표시했습니다.')
            else:
                print('좋아요 안함')
        else:
            print('잘못 입력하셨습니다.')

    def create_board(self):
        print('---------------- 게시글 생성 ------------------')
        title = input('제목 : ')
        content = input('내용 : ')
        writer = input('작성자 : ')
        password = input('수정용 비밀번호 : ')
        if input('확인 y : ') == 'y':
            self.boards.append([title, content, writer, password, 0, 0])
            print('게시글이 등록되었습니다.')
        else:
            print('취소되었습니다.')

    def modify_board(self):
        print('---------------- 게시글 수정 --------------------')
        print('수정하고자 하는 게시글 번호를 입력해주세요.')
        self.show_boards()
        if len(self.boards) == 0:
            print('게시글이 없습니다. 게시글을 생성해주세요.')
            return
        sel = input('>>> ')
        if sel.isdigit() and int(sel) in range(len(self.boards)):
            real_pw = self.boards[int(sel)][3]
            pw = input('비밀번호 : ')
            if real_pw == pw:
                print('수정하고자하는 항목 번호를 입력해주세요.')
                print(f'1. 제목 : {self.boards[int(sel)][0]}')
                print(f'2. 내용 : {self.boards[int(sel)][1]}')
                subSelect = input('>>> ')
                if subSelect == '1':
                    title = input('제목 : ')
                    self.boards[int(sel)][0] = title
                    print('제목이 수정되었습니다.')
                elif subSelect == '2':
                    content = input('내용 : ')
                    self.boards[int(sel)][1] = content
                    print('내용이 수정되었습니다.')
                else:
                    print('잘못 입력하셨습니다.')
            else:
                print('비밀번호가 다릅니다.')
        else:
            print('잘못 입력하셨습니다.')

    def delete_board(self):
        print('---------------- 게시글 삭제 --------------------')
        print('삭제하고자 하는 게시글 번호를 입력해주세요.')
        self.show_boards()
        if len(self.boards) == 0:
            print('게시글이 없습니다. 게시글을 생성해주세요.')
            return
        sel = input('>>> ')
        if sel.isdigit() and int(sel) in range(len(self.boards)):
            real_pw = self.boards[int(sel)][3]
            pw = input('비밀번호 : ')
            if real_pw == pw:
                self.boards.pop(int(sel))
                print('게시글이 삭제되었습니다.')
            else:
                print('비밀번호가 다릅니다.')
        else:
            print('잘못 입력하셨습니다.')

    def run(self):
        subrun = True
        while subrun:
            print('''
-------------------------
자료게시판에 진입하였습니다.

1. 게시글 목록
2. 게시글 상세 보기
3. 게시글 생성
4. 게시글 수정
5. 게시글 삭제
9. 자료게시판 종료''')
            subSelect = input('>>> ')
            if subSelect == '1':
                self.show_boards()
            elif subSelect == '2':
                self.show_board_detail()
            elif subSelect == '3':
                self.create_board()
            elif subSelect == '4':
                self.modify_board()
            elif subSelect == '5':
                self.delete_board()
            elif subSelect == '9':
                print('자료게시판 종료')
                subrun = False
            else:
                print('잘못 입력하였습니다.')