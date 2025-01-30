# 1. 사칙연산
# + - % * //
# // : 몫만
# A = int(input())
# B = int(input())
from math import floor, ceil, sqrt
from random import random, randrange, randint

A, B = 2,4
print(A + B) # 6
print(A - B) # -2
print(A * B) # 8
print(A / B) # 0.5
print(A % B) # 2
print(A // B) #0


# 숫자 처리 함수

# 절대값
abs(-5)  # 5

# 제곱
pow(2,4) # 2^2^2^2

#최대값
max(2,3,4,5) #5

#최솟값
min(2,3,4,5,) #2

#반올림
round(2.3) #2

#내림
floor(3.4)

#올림
ceil(2.1)

#제곱근
sqrt(16)


#랜덤함수
print(random()) # 0.0~1.0미만의 임의의 값 생성
print(random()*10)  # 0.0~10.0 미만의 임의의 값 생성
print(int(random()*10))  # 0~10 미만의 임의의 값 생성 (소수점 빼고)
print(int(random()*10)+1)  # 1~10 이하의 임의의 값 생성 (소수점 빼고)
print(int(random()*45)+1)  # 1~45 이하의 임의의 값 생성 (소수점 빼고)

print(randrange(1,46)) #1~46미만의 임의의 값 생성 (끝 값 포함하지 않음)

print(randint(1,45)) # 1~45 이하의 임의의 값 생성  (끝 값 포함)

#Quiz2
print("오프라인 스터디 모임 날짜는 매월",randint(4,28),"일로 선정되었습니다.")
