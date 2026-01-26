# 주민번호로 할 수 있는 일
# 입력받기
# 주민번호 검증 코드
# 생년월일 구분
# 나이
# 출생지역
# 남여 구분

# 701128-1258239
# 0123456789

#주민번호 입력
print("주민번호를 '-'포함  입력해주세요")
snum = input(">>>")

# 주민번호 검증


s0 = int(snum[0]) * 2
s1 = int(snum[1]) * 3
s2 = int(snum[2]) * 4
s3 = int(snum[3]) * 5
s4 = int(snum[4]) * 6
s5 = int(snum[5]) * 7
s7 = int(snum[7]) * 8
s8 = int(snum[8]) * 9
s9 = int(snum[9]) * 2
s10 = int(snum[10]) * 3
s11 = int(snum[11]) * 4
s12 = int(snum[12]) * 5

totals = s0+s1+s2+s3+s4+s5+s7+s8+s9+s10+s11+s12
mod = totals % 11
if mod == 10 :
    mod = 0
elif mod == 11 :
    mod = 1

if len(snum) == 14 :
    if snum[6] == "-":
        print("주민번호를 입력받았습니다.")
        if mod == int(snum[13]):
            print("주민번호가 유효합니다")
            print(mod)
        else:
            print("주민번호가 유효하지 않습니다.")
            print(mod)
            # exit()
        print("주민번호 : %s" %snum)
    else:
        print("'-'를 포함한 주민번호를 다시 입력해주세요")
        # exit()
else:
    print("주민번호 14자리를 다시 입력해주세요")
    # exit()

# 생년월일
year = snum[0:2]
month = snum[2:4]
day = snum[4:6]
print("생년 %s\n생월 %s\n생일 %s" %(year,month,day))

# 몇년생
if snum[7] in ["1","2","5","6"] :
    gen = "19" + year
elif snum[7] in ["9","0"] :
    gen = "18" + year
else :
    gen = "20" + year

print("%s년생입니다."%gen)

# 나이
age = 2026 - int(gen)
print("나이는 %d살 입니다." %(age))

# 성별구분
if snum[7] in ["1","3","5","7"]:
    gender = "남성"
elif snum[7] == "9" :
    gender = "외계인"
else :
    gender = "여성"

print("귀하는 %s 입니다."%gender)

# 출신지역
# 서울 00-08  부산 09-12    인천 13-15
# 경기 16-25  강원 26-34    충청 35-47
# 전라 48-66  경상 67-91    제주 92-95

local = ""

if int(snum[8:10]) < 9 :
    local = "서울"
elif int(snum[8:10]) < 13 :
    local = "부산"
elif int(snum[8:10]) < 16 :
    local = "인천"
elif int(snum[8:10]) < 26 :
    local = "경기"
elif int(snum[8:10]) < 35 :
    local = "강원"
elif int(snum[8:10]) < 48 :
    local = "충청"
elif int(snum[8:10]) < 67 :
    local = "전라"
elif int(snum[8:10]) < 92 :
    local = "경상"
elif int(snum[8:10]) < 96 :
    local = "제주"
else:
    local = "불명"

print("귀하의 출신지역은 %s입니다."%local)