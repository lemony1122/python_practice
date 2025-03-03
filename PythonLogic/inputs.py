import sys
print("Python","Java",file= sys.stdout) #표준출력
print("Python","Java",file= sys.stderr) #에러

print("Python","Java")
print("Python","Java",sep=",")
print("Python","Java",sep=" ")
print("Python","Java",sep="")
print("Python","Java",sep=" vs ")
print("Python","Java",sep=",", end="?")

# 시험 성적
scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items():    #items():  dictionary에서
    print(subject.ljust(8), str(score).rjust(4), sep=":")     #8칸 확보 후 왼쪽 정렬(ljst) , 4확보 오른쪽 정렬 (rjust)

#은행 대기 순번
# zfill(n) : n개 공간 확보 후 빈공간은 0으로
for num in range(1,21):
    print("대기번호: " + str(num).zfill(3))

#input으로 받는 값은 항상 문자열
answer = input("아무 값이나 입력하세요: ")
print("입력하신 값은 " + answer+ "입니다")

# 다양한 출력 포맷
# 1. 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))    # 한 칸 띄우기: 빈 공간으로 두고  > : 오른쪽 정렬  10: 총 공간  500을 출력
#2. 양수일때느 +로 표시, 음수일때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#3. 왼쪽 정렬, 빈칸으로 _ 채움
print("{0:_<10}".format(500))

#4. 3자리 마다 콤마 찍어주기
print("{0:,}".format(1000000000))

#5. 3자리 마다 콤마 찍어주기, +- 기호 붙여주기
print("{0:+,}".format(1000000000))

#6. 3자리 마다 콤마, 부호 붙이기, 자릿수 확보, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(10000))

#7. 소수점 출력
print("{0:f}".format(5/3))

#7-1 소수점 출력(2번쨰까지만 출력)
print("{0:2f}".format(5/3))

