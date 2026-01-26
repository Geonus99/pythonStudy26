import os
from tabulate import tabulate


headers = ["아이디", "비밀번호", "이름", "역할", "상태"]
FILE_NAME = "mems.txt"
run = True
session = None
members = []


def load_mems() :
    if not os.path.exists(FILE_NAME) :
        save_mems()
        print("파일생성")
        return

    with open(FILE_NAME, "r",encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("|")
            data[4] = True if data[4] == "True" else False
            members.append(data)


def save_mems():
    with open(FILE_NAME,"w",encoding="utf-8") as file:
        for member in members :
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n"
            file.write(line)


def main_menu() :
    print("""
===================
MBC 회원관리 프로그램
===================
1. 회원가입     2. 로그인     3. 로그아웃
4. 회원정보수정   5. 회원탈퇴
9. 프로그램 종료
""")

def members_add() :
    uid = input("id : ")
    for member in members :
        if member[0] == uid:
            print("이미존재")
            return
    pw = input("pw : ")
    name = input("name : ")

    print("1.admin 2.manager 3.user")
    role = "user"
    role_sel = input(">>>")
    if role_sel == "1" :
        role = "admin"
    elif role_sel == "2" :
        role = "manager"

    print(f"id : {uid} pw : {pw} name : {name} role : {role}")
    sel = input("(y/n) : ")
    if sel == "y" :
        members.append([uid,pw,name,role,True])
        save_mems()
        print("가입완료")
    else:
        print("취소")
        return

def member_delete() :
    user = zip(members)
    print(tabulate(user, headers,tablefmt="grid"))
    mem_del = input("삭제할 아이디 입력 : ")
    for i, member in enumerate(members) :
        if member[0] == mem_del :
            members.pop(i)
            save_mems()
            print("삭제완료")
            return

    print("존재하지않음")

def member_login() :
    log_id = input("id : ")
    for i, member in enumerate(members) :
        if member[0] == log_id :
            log_pw = input("pw : ")
            if member[1] == log_pw :
                session = member[0]
                print("로그인")
                return session


            print("비번잘못")

    print("존재x")





load_mems()
print(members)

while run :
    main_menu()
    select = input(">>>")
    if select == "1" :
        members_add()
    elif select == "2" :
        member_login()
    elif select == "5" :
        member_delete()