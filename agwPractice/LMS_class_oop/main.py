from MemberService import MemberService
from ScoreService import ScoreService
app =  MemberService()
app1 = ScoreService()
main_run = True
while main_run :
    # 회원에서 로그인한게 성적에서도 유지
    # 그러면 세션값을 계속 유지해줘야됨
    # 회원 세션에서 member에 정보가 들어가 있어서 그 함수 만들어서 성적에 들어가도
    # 유지되게
    print("""
1. 회원 2. 성적
    """)
    sel =  input(">> ")
    if sel == "1":
        app.run()
    elif sel == "2":
        app1.run()