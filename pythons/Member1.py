# 회원관리용 코드를 만든다.
# c -> 회원추가
# r -> 관리자일경우 (전체회원보기), 일반회원(로그인)
# u -> 관리자일경우 (회원차단, 암호변경문의), 일반회원(내정보수정, 암호변경)
# d -> 회원 탈퇴

# 잘못된 메뉴 여러번 가면 종료시키는거

# 메뉴구현
run = True # 프로그램 동작중을 관리하는 변수
idnum = None # 로그인한 현재 인덱스

"""
======================
엠비씨아카데미성적처리

1. 성적입력 # 관리자만 입력
2. 성적보기 # 일반회원은 개인조회 관리자는 전체조회
3. 성적수정 # 관리자만 수정
4. 성적삭제 # 관리자만 삭제
5. 프로그램 종료
"""

menu = """
============================
mbc 아카데미 회원 관리 프로그램
============================
1. 회원가입
2. 로그인
3. 회원보기
4. 내정보수정
5. 프로그램 종료
"""
adminmenu = """
============================
관리자 메뉴
============================
1. 회원가입(성적입력)
2. 회원보기(전체조회)
3. 내정보수정(성적수정)
4. 성적삭제
5. 프로그램 종료
"""
usermenu = """
=============================
사용자 메뉴
=============================
1. 회원보기(개인조회)
2. 내정보수정
3. 회원탈퇴
4. 프로그램 종료
"""
adminupdate = """
=============================
회원정보 수정
=============================
1. 사원번호 변경
2. 아이디 변경
3. 비밀번호 변경 x
4. 이름 변경 x
5. 이메일 변경 x
6. 관리자 변경
7. 프로그램 종료
"""
userupdate = """
=============================
회원정보 수정
=============================
1. 아이디 변경
2. 비밀번호 변경
3. 이름 변경
4. 이메일 변경
5. 프로그램 종료
"""

# 사용할 리스트 변수를 생성한다.
sns = [1, 2] # 사용자 관리번호
ids = ["kkw", "khj"] # 로그인용 id
passwords = ["1234", "4321"] # 로그인용 pw
names = ["관리자","임효정"] # 사용자명
emails = ["admin@mbc.com", "lhj@mbc.com"] # 이메일
admins = [True,False] # 관리자 유무 관리자 : True, 일반사용자 False
kors = [] # 국어 점수
engs = [] # 영어 점수
mats = [] # 수학 점수
tots = [] # 총점 빈 배열
avgs = [] # 평균 빈 배열
grades = [] # 학점 빈 배열


# ==================
# 첫메인화면
# ==================
while run :
    print(menu)
    select = input("1~5숫자를 입력하세요 : ")
    if select == "1":
        print("회원가입 메뉴에 진입하셨습니다.")
        sn = input("사번을 입력하세요 : ")
        id = input("아이디를 입력하세요 : ")

        # ===============
        # 아이디중복유무
        # ===============
        if id in ids:
            print("이미 존재하는 아이디입니다.")
            continue

        pw = input("암호를 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        email = input("이메일 주소를 입력하세요 : ")
        admin = False

        print("입력된 값을 확인하시고 y를 누르면 가입됩니다.")
        print("이름 : " + name)
        print("id : " + id)
        print("pw : " + pw)
        if input("y/n : ") == "y":
            sns.append(int(sn))
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            admins.append(admin)
            print("입력이 완료되었습니다.")
        else:
            print("처음부터 다시 진행하세요!!!")
    # =======================================
    # 로그인 메뉴
    # =======================================
    elif select == "2":
        print("로그인 메뉴에 진입하셨습니다.")
        id1 = input("아이디를 입력하세요 : ")
        pw1 = input("비밀번호를 입력하세요 : ")
        if id1 in ids :
            idnum = ids.index(id1)
            if pw1 == passwords[idnum] :

                # ========================================
                # 관리자 로그인
                # ========================================
                if admins[idnum] == True :
                    print("관리자로 로그인하셨습니다.")
                    run1 = True
                    while run1:
                        print(adminmenu)
                        select = input("1~5숫자를 입력하세요 : ")

                        # ===================================
                        # 관리자 회원가입
                        # ===================================
                        if select == "1":
                            print("회원가입 메뉴에 진입하셨습니다.")
                            run2 = True
                            while run2:
                                admin = input("관리자 여부를 1(관리자), 2(사용자)로 결정해주세요")
                                if admin == "1":
                                    admin = True
                                    run2 = False
                                elif admin == "2":
                                    admin = False
                                    run2 = False
                                else :
                                    print("다시하세요")
                            sn = input("사번을 입력하세요 : ")
                            id = input("아이디를 입력하세요 : ")
                            pw = input("암호를 입력하세요 : ")
                            name = input("이름을 입력하세요 : ")
                            email = input("이메일 주소를 입력하세요 : ")
                            print("입력된 값을 확인하시고 y를 누르면 가입됩니다.")
                            print("이름 : " + name)
                            print("id : " + id)
                            print("pw : " + pw)
                            if input("y/n : ") == "y":
                                sns.append(int(sn))
                                ids.append(id)
                                passwords.append(pw)
                                names.append(name)
                                emails.append(email)
                                admins.append(admin)
                                print("입력이 완료되었습니다.")
                            else:
                                print("처음부터 다시 진행하세요!!!")

                        # ==================================
                        # 관리자 전체 회원 조회
                        # ==================================
                        elif select == "2":
                            print("회원보기 메뉴에 진입하셨습니다.")
                            print("\n[전체 회원 목록]")
                            for i in range(len(ids)):
                                print(f"{i + 1}.{sns[i]} | {names[i]} | {ids[i]} | {emails[i]} | 관리자 : {admins[i]}")

                        # =====================================
                        # 관리자 내정보 수정
                        # =====================================
                        elif select == "3":
                            print("내정보수정 페이지 입니다.")
                            run2 = True
                            while run2:
                                print(adminupdate)
                                select = input("1~7 숫자를 입력해주세요 : ")
                                # =========================
                                # 사번변경
                                # =========================
                                if select == "1":
                                    print("사번을 변경할 회원의 아이디와 비밀번호를 입력해주세요.")
                                    idup = input("아이디 : ")
                                    if idup in ids :
                                        idnum = ids.index(idup)
                                        pwup = input("비밀번호 : ")
                                        if pwup == passwords[idnum] :
                                            sns[idnum] = input("변경하실 사번을 입력하세요 : ")
                                # =========================
                                # 아이디변경
                                # =========================
                                elif select == "2":
                                    idup = int(input("변경하실 아이디의 사원번호 : "))
                                    if idup in sns :
                                        idup = sns.index(idup)
                                        ids[idup] = input("변경하실 아이디를 입력해주세요 : ")

                                # =========================
                                # 관리자변경
                                # =========================
                                elif select == "6" :
                                    idup = int(input("권한 변경할 사원번호 : "))
                                    if idup in sns :
                                        idup = sns.index(idup)
                                        run3 = True
                                        while run3:
                                            admin = input("관리자 여부를 1(관리자), 2(사용자)로 결정해주세요 : ")
                                            if admin == "1":
                                                admin = True
                                                run3 = False
                                            elif admin == "2":
                                                admin = False
                                                run3 = False
                                            else:
                                                print("다시하세요")
                                        admins[idup] = admin
                                elif select == "7" :
                                    print("프로그램을 종료합니다.")
                                    run2 = False
                                elif select == "8":
                                    print("\n[전체 회원 목록]")
                                    for i in range(len(ids)):
                                        print(f"{i + 1}.{sns[i]} | {names[i]} | {ids[i]} | {emails[i]} | 관리자 : {admins[i]}")
                                else :
                                    print("1~7사이 값을 입력하세요!!!")

                        # ========================
                        # 회원 삭제
                        # ========================
                        elif select == "4":
                            """삭제 메뉴 채워 넣기"""
                        # =========================
                        # 첫메인화면으로가기
                        # =========================
                        elif select == "5":
                            print("로그아웃되셨습니다.")
                            idnum = None
                            run1 = False
                        else:
                            print("1~4사이 값을 입력하세요!!!!")

                # ============================
                # 일반 사용자
                # ============================
                else :
                    print("로그인되셨습니다.")
                    run5 = True
                    while run1:
                        print(usermenu)
                        select = input("1~3숫자를 입력해주세요 : ")
                        if select == "1":
                            print("\n[내 정보]")
                            print(f"이름 : {names[idnum]}")
                            print(f"아이디 : {ids[idnum]}")
                            print(f"이메일 : {emails[idnum]}")
                        elif select == "2":
                            print("내정보수정 메뉴에 진입하셨습니다.")
                        elif select == "3":
                            select = input("회원탈퇴를 위한 비밀번호를 입력해주세요 :\n")
                            if select in passwords:
                                select = passwords.index(select)
                                sns.pop(select)
                                ids.pop(select)
                                passwords.pop(select)
                                names.pop(select)
                                emails.pop(select)
                                admins.pop(select)
                                print("회원탈퇴 완료")
                                for i in range(len(ids)):
                                    print(f"{i + 1}.{sns[i]} | {names[i]} | {ids[i]} | {emails[i]} | 관리자 : {admins[i]}")

                        elif select == "4":
                            print("프로그램이 종료됩니다.")
                            idnum = None
                            run1 = False
                        else:
                            print("1~4사이 값을 입력하세요!!!!")
            else:
                print("잘못입력하셨습니다.")
        else:
            print("비밀번호가 틀립니다.")
    # =================================
    # 3. 회원보기
    # =================================
    elif select == "3":
        if idnum is None:
            print("먼저 로그인해주세요")
            continue
    elif select == "4":
        print("내정보수정 페이지 입니다.")
        if idnum is None:
            print("먼저 로그인해주세요")
    elif select == "5":
        print("회원가입 프로그램이 종료됩니다.")
        run = False
    else :
        print("1~5사이 값을 입력하세요!!!!")