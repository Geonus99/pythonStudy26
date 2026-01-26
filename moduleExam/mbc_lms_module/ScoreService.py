# 성적에 관한 CRUD를 구현
# 부메뉴와 함께 run() 메서드를 진행

class ScoreService:
    def __init__(self):
        # 클래스 생성 시 필요한 변수들..
        # 파일명,  등
        self.scores = []  # 모든 성적이 들어있는 2차원 리스트

    def getgrade(self, avg):  # 평균으로 등급 계산하기
        # class안에 있는 매서드가 getgrade인데, 파라미터인 avg를 불러와서 계산
        if avg > 90:
            return "A"

        elif avg > 80:
            return "B"

        elif avg > 70:
            return "C"

        else:
            return "F"
        # return하는 이유는 각각의 점수에 맞는 등급을 반환시키기 위해처리

    def run(self):
        # 부메뉴 구현 메서드
        subrun = True

        while subrun:
            print("""
-----------------------------------------
   1. 성적입력  2. 성적보기  3. 성적 수정
 4. 학생 정보 삭제  5. 성적확인 프로그램 종료
-----------------------------------------
            """)

            subselect = input(">>> ")

            if subselect == "1":
                print("\n[성적 입력]")

                sn = input("성적 입력할 학번 : ")
                name = input("성적 입력할 학생의 이름 : ")
                pyt = int(input("파이썬 점수 : "))
                db = int(input("데이터베이스 점수 : "))
                www = int(input("웹 점수 : "))

                tot = pyt + db + www
                avg = tot / 3

                # grade = ""

                grade = self.getgrade(avg)

                print("입력한 정보를 확인하세요.")
                print(f"학번 : {sn} | 이름 : {name}")
                print(f"파이썬 점수 : {pyt} | 데이터베이스 점수 : {db} | 웹 점수 : {www}")
                print(f"총점 : {tot} | 평균 : {avg} | 등급 : {grade}")

                if input("저장하시려면 y : ") == "y":
                    self.scores.append([sn, name, pyt, db, www, tot, avg, grade])
                    print(f"{name}님 성적 저장 완료")
                else:
                    print("입력이 취소되었습니다.")
                    print("처음부터 다시 시도해주세요.")


            elif subselect == "2":
                print("\n[성적 보기]")
                print("모든 학생의 성적을 확인합니다.")

                # for i in range(len(self.scores)):
                # print(self.scores[i])
                for idx, member in enumerate(self.scores):
                    print(
                        f"이름 : {member[1]} | 파이썬 : {member[2]} | 데이터베이스 : {member[3]} | 웹 : {member[4]} | 등급 : {member[7]}")

                if len(self.scores) == 0:
                    print("\n등록된 성적 정보가 없습니다.")
                    continue

            elif subselect == "3":
                print("\n[성적 수정]")

                sn = input("성적 수정할 학번 : ")

                if sn in self.scores[0]:
                    idx = self.scores[0].index(sn)
                    print("학번이 존재합니다.")
                    print(f"이름 : {self.scores[idx][1]}")
                    print(f"파이썬 : {self.scores[idx][2]} | 데이터베이스 : {self.scores[idx][3]} | 웹 : {self.scores[idx][4]}")

                    print("1. 파이썬 점수 수정")
                    print("2. 데이터베이스 점수 수정")
                    print("3. 웹 점수 수정")

                    sel = input("수정할 과목을 입력해주세요 : ")

                    if sel == "1":
                        self.scores[idx][2] = int(input("수정할 파이썬 점수 : "))
                        print("파이썬 점수 수정 완료")
                    elif sel == "2":
                        self.scores[idx][3] = int(input("수정할 데이터베이스 점수 : "))
                        print("데이터베이스 점수 수정 완료")
                    elif sel == "3":
                        self.scores[idx][4] = int(input("수정할 웹 점수 : "))
                        print("웹 점수 수정 완료")
                    else:
                        print("잘못 입력 하셨습니다.")

                    # 총점
                    self.scores[idx][5] = self.scores[idx][2] + self.scores[idx][3] + self.scores[idx][4]
                    # 평균
                    self.scores[idx][6] = self.scores[idx][5] / 3
                    # 등급
                    self.scores[idx][7] = self.getgrade(self.scores[idx][6])

                else:
                    print("입력하신 학번의 정보가 존재하지 않습니다.")

            elif subselect == "4":
                print("\n[학생 정보 삭제]")

                sn = input("정보 삭제할 학번 : ")

                if input(f"{sn}님의 모든 정보를 삭제하시려면 y : ") == "y":
                    # 순번이 없을때 idx = -1을 대입
                    idx = -1
                    for i, member in enumerate(self.scores):
                        if sn == member[0]:
                            idx = i
                            break

                        # idx = self.scores[0].index(sn)

                    if idx != -1:
                        self.scores.pop(idx)
                        print("삭제가 완료되었습니다.")
                else:
                    print("잘못 입력 하셨습니다.")

            elif subselect == "5":
                print("성적 확인 프로그램 종료")
                subrun = False

            else:
                print("잘못된 메뉴를 입력하셨습니다.")