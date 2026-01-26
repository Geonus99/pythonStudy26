# 비회원용 게시판을 만들어 보자.

# 프로젝트 목표
# c : 게시글 등록
# r : 게시글 전체 보기 (리스트)
# r : 게시글 자세히 보기
# u : 게시글 수정
# d : 게시글 삭제

# 사용할 변수 리스트 3 ( 전역 변수 : 프로그램 전반적으로 사용가능)
run = True # while문 프로그램 구동중!!
board_no = [] # 중복되지 않는 유일한 값, not null
board_title = [] # 게시글의 제목
board_content = [] # 게시글의 내용
board_writer = [] # 글쓴이
board_password = [] # 게시글의 암호(수정, 삭제)
board_hit = [] # 좋아요!!
board_visitCount = [] # 조회수!!

# 주메뉴
menu = """
================================
MBC 아카데미 비회원 게시판입니다.
         ⸜(◍'꒳'◍)⸝
         
1. 게시글 등록
2. 게시글 리스트 보기
3. 게시글 자세히 보기
4. 게시글 수정
5. 게시글 삭제
6. 게시글 검색
7. 게시판 프로그램 종료

"""

# 프로그램 실행문
while run :
    print(menu)
    # select는 while 문 안쪽에서만 활용되는 1회용 변수 : 지역변수
    select = input("1~6 입력 : ")
    #        input은 키보드로 입력한 값을 문자열로 전달함
    if select == "1" : # 키보드로 입력한 값이 1이면?
        print("게시글 등록")
        # 게시글 등록용 코드 추가
        # 게시글의 번호는 프로세스가 자동 처리
        # 키보드로 게시글을 받아 변수에 넣음
        title = input("제목 : ")
        content = input("내용 : ")
        writer = input("작성자 : ")
        password = input("암호 : ")

        # 넣은 정보를 확인한다.
        print(f"제목 : {title}, 내용 : {content}\n작성자 : {writer}, 암호 : {password}")
        choose = input("저장하려면 y를 누르세요 : ")

        if choose == "y" :

            board_title.append(title)
            board_content.append(content)
            board_writer.append(writer)
            board_password.append(password)

            # 제목의 리스트에서 인덱스를 추출하여 +1 한 값이 no
            # for idx in range(len(board_title)):
            #     board_no.append(idx+1)

            # 제목을 이용해서 번호를 생성하면 중복제목 문제발생
            # board_no 리스트의 길이를 활용하여 해결
            no = len(board_no) + 1

            board_no.append(no)
            board_hit.append(0) # 좋아요
            board_visitCount.append(0) # 조회수

            print(f"{no}번의 게시글이 등록 되었습니다.")
        else:
            print("다시 입력하세요")

    elif select == "2" :
        print("[게시글 전체 출력]")
        # 게시글 리스트 보기용 코드 추가

        print("--------------------------")
        print("번호\t 제목\t 작성자\t 조회수\t")
        # "{0:^5}".format("번호")
        # "{0:^5}".format("제목")
        # "{0:^5}".format("작성자")
        # "{0:^5}".format("조회수")
        print("--------------------------")

        if len(board_no) == 0 :
            print("등록된 게시물이 없습니다.")
            continue # while문으로 돌아감

        for i in range(len(board_no)) : # 게시글의 개수만큼 반복 ( 0~게시물수까지 인덱스 처리용)
            print(f"{board_no[i]}\t {board_title[i]}\t {board_writer[i]}\t {board_visitCount[i]}")
            #           번호              제목              작성자                 조회수

    elif select == "3" :
        print("[게시글 자세히 보기]")
        # 게시글 자세히 보기 코드 추가
        bno = int(input("게시글 번호 : "))

        if bno in board_no :
            print("게시물을 찾았습니다.")
            idx = board_no.index(bno) # 리스트에서 게시물의 인덱스 값을 찾아옴

            board_visitCount[idx] += 1 # 조회수 1 증가

            print("------------------------")
            print(f"번호 : {board_no[idx]}")
            print(f"제목 : {board_title[idx]}")
            print(f"내용 : {board_content[idx]}")
            print(f"작성자 : {board_writer[idx]}")
            print(f"조회수 : {board_visitCount[idx]}")
            print(f"좋아요 : {board_hit[idx]}")
            print("-------------------------")

            if input("좋아요 누르기(y) : ") == "y":
                board_hit[idx] += 1
                print("좋아요 +1")
            else:
                print("아쉽습니다. 다음에 더 좋은 게시글이 될겁니다.")


        else :
            print("해당번호에 게시글이 없습니다.")

    elif select == "4" :
        # 게시글 수정 코드 추가
        print("[게시글 수정]")
        number = int(input("수정할 게시글의 번호 : "))
        if number in board_no :
            idx = board_no.index(number)
            pw = input("수정할 게시글의 비밀번호 : ")
            if pw == board_password[idx] :
                title = input("제목 수정 : ")
                content = input("내용 수정 : ")

                board_title[idx] = title
                board_content[idx] = content

                print("수정되었습니다.")
            else:
                print("비밀번호가 틀립니다.")
        else :
            print("게시글이 존재하지 않습니다.")


    elif select == "5" :
        # 게시글 삭제 코드 추가
        print("[게시글 삭제]")
        number = int(input("삭제할 게시글의 번호 : "))
        if number in board_no :
            idx = board_no.index(number)
            number2 = input("삭제할 게시글의 비밀번호 : ")
            if number2 == board_password[idx] :
                board_no.pop(idx)
                board_title.pop(idx)
                board_content.pop(idx)
                board_writer.pop(idx)
                board_password.pop(idx)
                board_hit.pop(idx)
                board_visitCount.pop(idx)

                print("삭제됐습니다.")
            else:
                print("비밀번호가 틀립니다.")
        else :
            print("게시물이 존재하지 않습니다.")
        # 게시글 삭제 코드 추가

    elif select == "6":
        print("[게시글 검색]")
        print("1. 제목으로 검색")
        print("2. 작성자로 검색")

    elif select == "7" :
        print("[비회원게시판 프로그램 종료]")
        print("")
        run = False

    else :
        print("1~6 숫자 입력해주세요.")