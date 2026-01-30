from enum import member

from lms.domain import Member
from lms.common import Session

class MemberService:

    @classmethod
    def load(cls):
        conn = Session.get_connection()
        try :
            with conn.cursor() as cursor:
                cursor.execute("select count(*) as cnt from members")
                count = cursor.fetchone()['cnt']
                print(f"시스템에 현재 등록된 회원수는 {count}명 입니다.")
        except:
            print("MemberService.load() 메서드 오류 발생...")

        finally:
            print("데이터베이스 접속 종료됨..")
            conn.close()

    @classmethod
    def login(cls):
        print("\n[로그인]")
        uid = input("ID : ")
        pw = input("Password : ")

        conn = Session.get_connection()

        try:
            with conn.cursor() as cursor:
                sql = "select * from members where uid = %s and password = %s"
                cursor.execute(sql, (uid, pw))
                row = cursor.fetchone()
                if row:
                    member = Member.from_dict(row)

                    if not member.active:
                        print("비활성화된 계정입니다.")
                        return

                    Session.login(member)
                    print(f"{member.name}님 로그인 성공 [{member.role}]")
                else:
                    print("아이디 또는 비밀번호가 틀렸습니다.")
        except:
            print("MemberService.login()메서드 오류발생...")
        finally:
            conn.close()

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("\n[알림] 현재 로그인 상태가 아닙니다.")
            return

        Session.logout()
        print("\n[성공] 로그아웃 되었습니다. 안녕히가세요")

    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("ID : ")
        conn = Session.get_connection()
        try :
            with conn.cursor() as cursor:
                check_sql = "select id from members where uid = %s"
                cursor.execute(check_sql, (uid,))
                if cursor.fetchone():
                    print("이미 존재하는 아이디입니다.")
                    return
                pw = input("Password : ")
                name = input("Name : ")

                insert_sql = "insert into members (uid, password, name) values (%s, %s, %s)"
                cursor.execute(insert_sql, (uid, pw, name))
                conn.commit()
                print("회원가입 완료")
        except Exception as e:
            conn.rollback()
            print(f"회원가입 오류 : {e}")
        finally:
            conn.close()

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요")
            return
        member = Session.login_member
        print(f"{member.name}님({member.role})")
        print(f"ID : {member.uid}")
        print(f"Password : {member.pw}")

        sel = input("[내 정보 수정]\n1.이름 변경 2.비번 변경 3. 계정비활성 및 탈퇴 0.취소")
        if sel == "1":
            member.name = input("Name : ")
        elif sel == "2":
            member.pw = input("Password : ")
        elif sel == "3":
            cls.delete()
        else:
            return

        conn = Session.get_connection()
        try :
            with conn.cursor() as cursor:
                sql = "update members set name = %s, password = %s where uid = %s"
                cursor.execute(sql, (member.name, member.pw, member.uid))
                conn.commit()
                print("정보수정완료")
        finally:
            conn.close()

    @classmethod
    def delete(cls):
        sel = input("\n[회원탈퇴]\n1.완전 탈퇴 2. 계정 비활성화\n")
        member = Session.login_member
        conn = Session.get_connection()
        try :
            with conn.cursor() as cursor:
                if sel == "1":
                    sql = "DELETE FROM members WHERE id = %s"
                    cursor.execute(sql, (member.id,))
                    print("회원 탈퇴 완료")
                elif sel == "2":
                    sql = "update members set active = FALSE where id = %s"
                    cursor.execute(sql, (member.id,))
                    print("비활성화 완료")

                conn.commit()
                Session.logout()
        finally:
            conn.close()

    @classmethod
    def admin_menu(cls):
        print("""
     ᕱ⑅ᕱ
    (¬`‸´¬)         관리자 메뉴  
    /      / +=={:::::::::::::::::>

    1. 회원조회
    2. 회원정보변경
    3. 회원삭제
    9. 돌아가기
        """)

    @classmethod
    def admin(cls):
        while True:
            cls.admin_menu()
            sel = input(">>> ")
            if sel == "1":
                cls.show_member()
            elif sel == "2":
                pass
            elif sel == "3":
                pass
            else:
                return

    @classmethod
    def show_member(cls):
        conn = Session.get_connection()
        try :
            with conn.cursor() as cursor:
                sql = "select * from members"
                cursor.execute(sql)
                all = cursor.fetchall()
                print(all)
        finally:
            conn.close()
