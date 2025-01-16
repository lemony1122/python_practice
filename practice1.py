# 애완동물을 소개합니다
animal = "강아지"
name = "연탄"
age = 4
hobby= "산책"
is_adult = age > 3

print("우리집" + animal + "의 이름은 " + name+"이에요")
# str로 타입 변환
hobby = "공놀이"
print(name+"은 "+ str(age) +"살이며, " + hobby+"를 좋아해요")
# 콤마를 쓰면 뒤에 무조건 빈칸이 들어감
print(name,"은",age,"살이며, ", hobby,"를 좋아해요")
# boolean도 str로 감싸야함
print(name+"은 어른일까요?" + str(is_adult))

# 주석
'''여러문장을
주석처리할때
'''

# 미니 퀴즈
station1 = "사당"
station2 = "신도림"
station3 = "인천공항"
print(station1,"행 열차가 들어오고 있습니다.")
print(station2,"행 열차가 들어오고 있습니다.")
print(station3,"행 열차가 들어오고 있습니다.")