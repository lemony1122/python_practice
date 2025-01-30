# 튜플 : 내용 변경이나 추가 안됨, 속도는 list 보다 빠름

# 메뉴판: 2가지만, 절대 변경이 없음
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)
(name,age,hobby) = ("김종국",20,"코딩")
print(name,age,hobby)
