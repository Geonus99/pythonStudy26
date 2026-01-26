# 주민번호를 입력 받아 생년월일 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 주민번호 검증 코드
# 나이 계산
# 처리0 : 주민번호 입력 검증 -> 14글자인지? 7번째에 - 유모
# 처리1 : 생년월일을 추출! -> 1,2,5,6 1900년생, 나머지 2000년생
# 처리2 : 주민번호 8번째 글자를 추출 -> 남여 구분
# 처리3 : 9~10번째 글자를 추출 -> 출생지역


print("주민번호를 입력하세요!!(-포함 14자)")
ssn = input(">>> ")
# ssn = "991210-1234567"
#        0123456789

# 입력된 주민번호 검증 코드
if len(ssn) == 14 : # 키보드로 입력된 문자열이 14자?
    print("14자 입력이 확인 되었습니다.")
    if ssn[6] == "-":
        print("주민번호 7번째 구문자 인식 완료")
    else:
        print("주민번호 7번쨰 구문자가 입력되지 않음")
        print("프로그램을 처음부터 다시 실행하세요")
        exit(0)  # 강제 종료
else:
    print("주민번호 14자가 입력되지 않았습니다.")
    exit(0) # 강제 종료


# 주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6 1900년생
# 나머지는 2000년생

year = ssn[0:2] # 생년
month = ssn[2:4] # 생월
day = ssn[4:6] # 생일

fullYear = "" # if안쪽에서 변수를 선언하면 버그가 발생할 수 있음
# ""null 처리용
if ssn[7] in ["1","2","5","6"] :
    fullYear = "19"+year
else :
    fullYear = "20"+year

print("귀하의 생년은 : %s년생 입니다." % fullYear)


# 나이 계산 해보자
age = 2026 - int(fullYear)
print("귀하의 나이는 " + str(age) + "세 입니다.")
#                   print는 문자열 + 숫자로 출력 오류가 발생
#                             문자열로 변환(강제타입변환) -> str(age)


# 주민번호 8번째 숫자가 1,3,5,7이면 남자, 나머지는 여자
gender = "" # 성별 null
if ssn[7] in ["1","3","5","7"] :
    gender = "남성"
elif ssn[7] == "9":
    gender = "외계인"
else :
    gender = "여성"

print("귀하는 " + gender + "으로 판단됩니다.")

# 8~9번째
# 서울 00-08  부산 09-12    인천 13-15
# 경기 16-25  강원 26-34    충청 35-47
# 전라 48-66  경상 67-91    제주 92-95
local = "" # 출생지를 판다하는 문자열
ssnLocal = ssn[8:10]  # 출생지 코드가 추출


if int(ssnLocal) < 9 :
    local = "서울"
elif int(ssnLocal) < 13 :
    local = "부산"
elif int(ssnLocal) < 16 :
    local = "인천"
elif int(ssnLocal) < 26 :
    local = "경기"
elif int(ssnLocal) < 35 :
    local = "강원"
elif int(ssnLocal) < 48 :
    local = "충청"
elif int(ssnLocal) < 67 :
    local = "전라"
elif int(ssnLocal) < 92 :
    local = "경상"
elif int(ssnLocal) < 96 :
    local = "제주"
else :
    local = "불명"
print("귀하의 출신지는 " + local + "입니다.")