sentence1 ='풍선'
print(sentence1)
print("나비")

#반복
print("ㅋ"*9)

#여러 문자 출력
sentence2 = """
나는 소년이고 
파이썬은 쉬워요
"""
print(sentence2)


# 슬라이싱
social_number = "782913-283192"
print("성별: "+ social_number[7])
print("연: "+ social_number[0:2])
print("월: "+ social_number[2:4])
print("일: "+ social_number[4:6])

# 처음부터 몇번째까지
print(social_number[:6])
# 앞에서부터
print(social_number[7:])  # 7부터 끝까지
# 뒤에서부터
print(social_number[-7:])


#문자열 처리 함수
python = 'Phyton is Amazing'

print(python.upper())  #모두 대문자
print(python.lower())  #모두 소문자
print(python[0].isupper()) #첫번째 문자가 대문자인지
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)

print(python.find("Java"))  #없을때는 -1
# print(python.index("Java")) # 오류가 남

print(python.count("n")) # 몇번 나오는지



# 문자열 포맷
print("a"+"Basics")
print("a","Basics")

# 방법 1
print("나는 %d살입니다." % 20)  # %d : 숫자를 받겠다
print("나는 %s를 좋아합니다." % "파이썬")   # %s: 문자열을 받겠다
print("나는 %c를 좋아합니다." % "A")   # %c: 문자 하나만(char)을 받겠다
# %s는 어떤 자료형도 받는다
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아합니다" % ("파란","노랑"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다." .format("파랑","노랑"))
print("나는 {0}색과 {1}색을 좋아합니다." .format("파랑","노랑"))
print("나는 {1}색과 {0}색을 좋아합니다." .format("파랑","노랑"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아합니다" .format(age=20, color="빨강"))
print("나는 {age}살이며, {color}색을 좋아합니다" .format(color="빨강",age=20))

# 방법 4 (python v3.6 이상)
age= 21
color = "파스텔톤"
print(f"나는 {age}살이며, {color}색을 좋아해요.")




# 탈출 문자
# \n : 줄 바꿈
# print("백문이 불여일견
      # 백견이 불여일타")  오류
print("백문이 불여일견\n백견이 불여일타")

# 저는 "한희준"입니다.
# print("저는 "한희준"입니다.")  오류 : 안에 있는 한희준도 문자열로 인식
print("저는 '한희준'입니다.")

# 방법 1 : 큰 따옴표를 꼭 쓰고 싶으면 작은 따옴표로 시작할 수 있음
print('저는 "한희준"입니다.')
# 방법 2 : 역슬래시(\", \') 사용
print('저는 \"한희준\"입니다.')
# 방법 3 : \\ --> 문장안에서는 \ 하나만 출력
print("C:\\")   #C:\
print("C:\\\\")  #C:\\


# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \Basics: 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t: 탭
print("Red\tApple")


# Quiz3
def createPassword(url):
    index = url.find("//")   #url.replace("http://","")
    url = url[index+2:url.find(".")]
    # return print(url[:3]+str(len(url))+str(url.count("e"))+"!")
    password = url[:3]+str(len(url))+str(url.count("e"))+"!"
    return print(f"{url}의 비밀번호는 {password}입니다.")

createPassword("http://naver.com")