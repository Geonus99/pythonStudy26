"""
+++++++++++참고사항+++++++++++++++
회원가입과 성적처리 연동

회원가입	-> 일반사용자

로그인	-> 관리자
		-> 일반

회원보기	-> 전체조회 (관리자)
		-> 개인조회 (일반)

내정보수정	-> 제한없음 (관리자)
		-> 비밀번호변경은 가능하나 사번이나 관리자 유무 같은건 수정불가 (일반)

회원삭제	-> 관리자

회원탈퇴	-> 일반
"""
# ===========
# 인터페이스
# ===========
MainMenu = """
==================
대보정보통신
==================
1. 로그인
2. 회원가입
3. 프로그램종료
"""

AdminMenu = """
==================
관리자 메뉴
==================
1. 회원조회
2. 회원정보수정
3. 회원삭제
4. 프로그램종료
"""

UserMenu = """
==================
사용자 메뉴
==================
1. 개인정보조회
2. 개인정보수정
3. 회원탈퇴
4. 프로그램종료
"""

AdminUp = """
=============================
회원정보 수정
=============================
1. 사원번호 변경
2. 아이디 변경
3. 국어 점수 변경
4. 관리자 변경
5. 프로그램 종료
"""

# 학번, 아이디, 비번, 이름, 생년월일, 국어, 영어, 수학, 총점, 평균, 등급, 관리자
sns = ["1","2"]
ids = ["1","2"]
pws = ["1","2"]
names = ["aaa","bbb"]
snums = ["991212-1234567","000101-3456789"]
kors = [50,80]
engs = [50,80]
mats = [50,80]
tots = [150,240]
avgs = [50,80]
grades = ["F","B"]
values = [True,False]

idnum = None # 회원식별용 변수
run = True # 프로그램 전체 반복을 위한 변수

# ============
# 메인
# ============
while run:
    run01 = True  # 내부 메뉴 반복을 위한 변수
    print(MainMenu)
    select = input("1~3 선택 : ")
    # ===========
    # 로그인
    # ===========
    if select == "1" :
        id = input("아이디를 입력해주세요 : ")
        if id in ids :
            idex = ids.index(id) # 리스트 매치용 변수
            pw = input("비밀번호를 입력해주세요 : ")
            if pw in pws :
                print("로그인되셨습니다.")
                # ===========
                # 관리자 로그인
                # ===========
                if values[idex] == True :
                    while run01 :
                        print(AdminMenu)
                        select = input("1~4 선택 : ")
                        # =========
                        # 회원조회
                        # =========
                        if select == "1" :
                            print("전체 회원 조회하기")
                            for i in range (len(sns)) :
                                print(f"학번 : {sns[i]}, 아이디 : {ids[i]}, 이름 : {names[i]}, 주민번호 : {snums[i]}, 평균 : {grades[i]}")
                        # =========
                        # 회원수정
                        # =========
                        elif select == "2" :
                            print("회원정보수정")
                            # 관리자는 하나로 일반은 한번에로 ㄱㄱ 다 만들면 지워 헷갈림
                            # ===============
                            # 회원정보수정메뉴
                            # ===============
                            run02 = True
                            while run02 :
                                print(AdminUp)
                                select = input("1~5 입력 : ")
                        # =========
                        # 회원삭제
                        # =========
                        elif select == "3" :
                            print("회원삭제")
                            sndel = input("삭제하실 사원번호를 입력하세요 : ")
                            if sndel in sns :
                                sndel = sns.index(sndel)
                                sns.pop(sndel)
                                ids.pop(sndel)
                                pws.pop(sndel)
                                names.pop(sndel)
                                snums.pop(sndel)
                                kors.pop(sndel)
                                engs.pop(sndel)
                                mats.pop(sndel)
                                tots.pop(sndel)
                                avgs.pop(sndel)
                                grades.pop(sndel)
                                values.pop(sndel)
                                print("삭제완료")
                                for i in range (len(sns)) :
                                    print(f"학번 : {sns[i]}, 아이디 : {ids[i]}, 이름 : {names[i]}, 주민번호 : {snums[i]}, 평균 : {grades[i]}")
                            else :
                                print("사원번호를 다시 입력하세요")
                        # =========
                        # 탈출
                        # =========
                        elif select == "4" :
                            print("나가기")
                            idex = None # 로그인 초기화
                            run01 = False
                        else :
                            print("1~4 입력")
                # ===========
                # 사용자 로그인
                # ===========
                else :
                    while run01 :
                        print(UserMenu)
                        select = input("1~4 선택 : ")
            else:
                print("비밀번호가 틀립니다.")
        else :
            print("존재하지 않는 아이디입니다.")

    # ==============
    # 회원가입
    # ==============
    elif select == "2" :
        print("회원가입")
        sn = input("사원번호를 입력하세요 : ")
        id = input("아이디를 입력하세요 : ")
        pw = input("비밀번호를 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        snum = input("주민번호를 입력하세요 : ")
        kor = int(input("국어점수를 입력하세요 : "))
        eng = int(input("영어점수를 입력하세요 : "))
        mat= int(input("수학점수를 입력하세요 : "))

        tot = kor + eng + mat
        avg = tot / 3

        if avg >= 90 :
            grade = "A"
            grades.append(grade)
        elif avg >= 80 :
            grade = "B"
            grades.append(grade)
        else :
            grade = "F"
            grades.append(grade)

        sns.append(sn)
        ids.append(id)
        pws.append(pw)
        names.append(name)
        snums.append(snum)
        kors.append(kor)
        engs.append(eng)
        mats.append(mat)
        tots.append(tot)
        avgs.append(avg)
        grades.append(grades)


    elif select == "3" :
        print("프로그램을 종료합니다.")
        run = False
    else :
        print("1~3 입력해주세요")
