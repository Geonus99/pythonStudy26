# 회원에 대한 crud를 구현
# 부메뉴와 함께 run()메서드를 진행

class MemberService:
    def __init__(self):
        # 클래스 생성 시 필요한 변수들....
        self.members = [['kkw', '1234', '김기원', 'admin', True]]  # 모든 회원이 들어 있는 2차원 리스트
        self.session = None

    def run(self):
        # 부메뉴 구현 메서드
        subrun = True
        while subrun:
            print('''
            ------------------------------------
            1. 로그인
            2. 회원가입
            3. 회원수정
            4. 회원탈퇴
            5. 로그아웃
            6. 관리자 메뉴

            9. 회원 서비스 종료
            ''')
            subSelect = input('>>> : ')
            if subSelect == '1':
                print('로그인 메서드 호출')
                self.member_login()

            elif subSelect == '2':
                print('회원가입 메서드 호출')
                self.member_add()

            elif subSelect == '3':
                print('회원 수정 메서드 호출')
                self.member_modify()

            elif subSelect == '4':
                print('회원 탈퇴 메서드 호출')
                self.member_delete()

            elif subSelect == '5':
                print('로그아웃 메서드 호출')
                self.member_logout()

            elif subSelect == '6':
                print('관리자 메뉴 호출')
                self.admin_menu()

            elif subSelect == '9':
                print('회원 서비스 종료')
                subrun = False

            else:
                print('잘못된 선택입니다.')

    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    def member_login(self):  # 로그인 메서드
        print('로그인 메뉴')
        uid = input('아이디 : ')
        pw = input('비밀번호 : ')
        for idx, member in enumerate(self.members):
            if member[0] == uid:
                if member[4] == False:
                    print('비활성화 계정입니다.')
                    return

                if member[1] == pw:
                    self.session = idx
                    print(f'{member[2]}님께서 로그인 하셨습니다.')
                    return

                else:
                    print('비밀번호가 다릅니다.')
                    return

        print('존재하지 않는 아이디입니다.')

    def member_logout(self):  # 로그아웃 메서드
        if self.session == None:
            print('로그인 상태가 아닙니다.')
            return

        self.session = None
        print('로그아웃 완료')

    def member_add(self):  # 회원 가입 메서드
        print('회원 가입 메뉴')
        uid = input('아이디 : ')
        for idx, member in enumerate(self.members):
            if member[0] == uid:
                print('이미 존재하는 아이디입니다.')
                return

        pw = input('비밀번호  :')
        name = input('이름 : ')
        role = 'user'

        self.members.append([uid, pw, name, role, True])
        print('회원 가입 완료')

    def member_modify(self):  # 회원 정보 수정 메서드
        if self.session == None:
            print('로그인 후 이용가능합니다.')
            return

        print('회원 정보 수정')
        print('1. 이름 변경')
        print('2. 비밀번호 변경')

        select = input('>>> : ')
        if select == '1':
            self.members[self.session][2] = input('새 이름 : ')
            print('수정 완료')
            print(f'수정 후 이름 : {self.members[self.session][2]}')
        elif select == '2':
            self.members[self.session][1] = input('새 비밀번호 : ')
            print('수정 완료')
            print(f'수정 후 비밀번호 : {self.members[self.session][1]}')
        else:
            print('잘못된 입력입니다.')

    def member_delete(self):  # 회원 탈퇴 메서드
        if self.session == None:
            print('로그인 후 이용가능합니다.')
            return

        if self.members[self.session][3] == 'admin':
            print('관리자는 회원탈퇴/비활성화가 불가능합니다.')
            return

        print('회원 정보 삭제')
        print('1. 회원 탈퇴')
        print('2. 회원 비활성화')

        select = input('>>> : ')
        if select == '1':
            self.members.pop(self.session)
            print('처리 완료')
        elif select == '2':
            self.members[self.session][4] = False
            print('처리 완료')
        else:
            print('잘못된 입력입니다.')

        self.session = None

    def admin_menu(self):  # 관리자 메뉴 메서드
        while True:  # 관리자 메뉴 반복 while문
            if self.session == None:
                print('로그인 후 이용가능합니다.')
                return

            if self.members[self.session][3] != 'admin':  # 권한이 관리자가 아니면 접근 불가
                print('관리자만 이용 가능합니다.')
                return

            print('''
            ---------------------------------------------
            1. 회원 전체 보기
            2. 회원 비활성화 해제
            3. 회원 강제 탈퇴
            4. 회원 비번 변경
            5. 뒤로 가기
            ''')
            choice = input('>>> : ')

            if choice == '1':
                print('회원 전체보기')
                print('이름\t 아이디\t 비번\t 권한\t활성화}')
                for idx, member in enumerate(self.members):
                    print(f'{member[2]}|\t{member[0]}|\t{member[1]}|\t{member[3]}|\t{member[4]}|')

            elif choice == '2':
                print('회워 비활성화 해제')
                fid = input('비활성화를 해제 할 회원의 아이디를 입력해주세요. : ')
                for idx, member in enumerate(self.members):
                    if fid == member[0]:
                        member[4] = True
                        break

                else:
                    print('존재하지 않는 아이디입니다.')

            elif choice == '3':
                print('회원 강제 탈퇴')
                delid = input('강제 탈퇴를 진행 할 회원의 아이디를 입력해주세요. : ')
                for idx, member in enumerate(self.members):
                    if delid == member[0]:
                        self.members.pop(idx)
                        print('회원 정보 삭제 완료')
                        break

                else:
                    print('존재하지 않는 아이디입니다.')

            elif choice == '4':
                print('회원 비번 변경')
                mid = input('비밀번호를 변경 할 회원의 아이디를 입력해주세요. : ')
                for idx, member in enumerate(self.members):
                    if mid == member[0]:
                        member[1] = input('새 비밀번호 : ')
                        print('회원 비밀번호 수정 완료')
                        break

                else:
                    print('존재하지 않는 아이디입니다.')

            elif choice == '5':
                return

            else:
                print('잘못된 입력입니다.')