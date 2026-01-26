from tabulate import tabulate


run = True
session = None

names = ["김기원","임효정","안건우"]
ids = ["kkw", "ihj", "agw"]
pws = ["1234", "5678","1111"]
roles = ["admin", "manager", "user"] # admin, manager, user
active = [True, True, True] # True, False

headers = ["아이디", "비밀번호", "이름", "역할", "상태"]
data = zip(names, ids, pws, roles, active)


# member
def member_add() :
    print("===회원가입===")
    user_id = input("아이디 : ")
    if user_id in ids :
        print("이미 존재하는 아이디")
        return

    user_pw = input("비밀번호 : ")
    user_name = input("이름 : ")

    user_role = "user"
    print(f"아이디 : {user_id} 비밀번호 : {user_pw} 이름 :{user_name}")
    add_select = input("가입하시려면 y : ")
    if add_select == "y" :
        names.append(user_name)
        ids.append(user_id)
        pws.append(user_pw)
        roles.append(user_role)
        active.append(True)
    else:
        print("가입되지 않았습니다.")

def member_login():
    global session
    if session is not None :
        print(f"현재 로그인 사용자 : {names[session]}")
        return

    print("===로그인===")
    user_id = input("아이디 : ")
    if user_id in ids :
        idx = ids.index(user_id)
        user_pw = input("비번 : ")
        if user_pw == pws[idx] :
            session = idx
            print(f'"{ids[idx]}"님 로그인 되셨습니다')
        else:
            print("비밀번호가 틀림")
    else:
        print("존재하지 않는 아이디")

def member_logout():
    global session
    if session is not None:
        print(f"'{names[session]}'님 로그아웃 완료\n다음에 또 방문해주세요")
        session = None
    else:
        print("로그인 후 이용해주세요")
        return

def member_modify():
    global session
    if session is not None:
        if not active[session] :
            print("정지된 사용자입니다.")
            return

        if roles[session] == "admin":
            act1 = map(lambda act : "활성화" if act is True else "비활성화", active)
            rol1 = map(lambda rol : "관리자" if rol == "admin" else "매니져" if rol == "manager" else "사용자", roles)
            user = zip(ids,pws,names,rol1,act1)
            print(tabulate(user, headers,tablefmt="grid"))


            modify_id = input("변경할 회원정보 아이디 입력 : ")
            if modify_id in ids :
                mdx = ids.index(modify_id)
                print(f"1.아이디 : {ids[mdx]}\n2.비밀번호 : .{pws[mdx]}\n3.이름 : {names[mdx]}\n4.권한 : {roles[mdx]}\n5.활성화 : {active[mdx]}")
                sel = input("변경하실 정보를 선택하세요 (1~5) : ")
                if sel == "1":
                    ids[mdx] = input("아이디 : ")
                elif sel == "2":
                    pws[mdx] = input("비번 : ")
                elif sel == "3":
                    names[mdx] = input("이름 : ")
                elif sel == "4":
                    roles_menu()
                    roles_select = input("관리자변경\t>>>")
                    if roles_select == "1":
                        roles[mdx] = "admin"
                    elif roles_select == "2":
                        roles[mdx] = "manager"
                    else:
                        roles[mdx] = "user"
                elif sel == "5":
                    active_menu()
                    act_select = input(">>>")
                    if act_select == "1":
                        active[mdx] = True
                    elif act_select == "2":
                        active[mdx] = False
                else:
                    print("다시 확인해주세요")
            else:
                print("다시 확인해주세요")
                return

        elif roles[session] == "manager":
            act_name = input("중지시킬 사용자 아이디 : ")
            if act_name in ids :
                tdx = ids.index(act_name)
                active_menu()
                act_select = input(">>>")
                if act_select == "1":
                    active[tdx] = True
                elif act_select == "2":
                    active[tdx] = False
            else:
                print("다시 확인해주세요")
        else:
            print("내 정보 수정")
            print("1. 비밀번호 변경")
            print("2. 이름 변경")
            sel = input("선택 : ")
            if sel == "1":
                pws[session] = input("변경할 비밀번호 : ")
            elif sel == "2":
                names[session] = input("변경할 이름 : ")
            else:
                print("변경 취소")
                return
            print("변경완료")
    else:
        print("로그인 후 이용해주세요")
        return

def member_delete():
    global session
    if session is not None :
        if roles[session] == "admin":
            print(f"{ids} | {pws} | {names} | {roles} | {active}")
            del_select = input("탈퇴시킬 아이디를 입력해주세요 : ")
            if del_select in ids :
                rem = ids.index(del_select)
                ids.pop(rem)
                pws.pop(rem)
                names.pop(rem)
                roles.pop(rem)
                active.pop(rem)
                print('삭제 완료')
            else:
                print("다시 확인해주세요")
        else:
            print(f'"{names[session]}님 탈퇴하시겠습니까?')
            del_select = input("(y/n) : ")
            if del_select == "y" :
                ids.pop(session)
                pws.pop(session)
                names.pop(session)
                roles.pop(session)
                active.pop(session)
                print("탈퇴 완료")
                session = None
            else:
                print("탈퇴하지 않습니다.")

    else:
        print("로그인후 이용가능합니다.")

# menu
def main_menu() :
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다 ====
    1. 회원가입   2. 로그인   3. 로그아웃
    4. 회원정보수정   5.회원탈퇴
    9. 프로그램 종료
""")

def roles_menu() :
    print(f"""
1. 관리자  2. 매니져  3. 일반
""")

def active_menu() :
    print(f"""
1. True    2. False
""")

# main
while run:
    main_menu()
    select = input(">>>")
    if select == "1" :
        member_add()

    elif select == "2" :
        member_login()

    elif select == "3" :
        member_logout()

    elif select == "4" :
        member_modify()

    elif select == "5" :
        member_delete()

    elif select == "9" :
        run = False
    else:
        print("다시")
