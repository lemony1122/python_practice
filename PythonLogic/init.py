
# 기본 값

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 :  {2}"\
          .format(name, age, main_lang))

profile("유재석",20,"java")

# 같은 학년
def profile(name, age=17, main_lang="python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 :  {2}"\
          .format(name, age, main_lang))

profile("유재석")

# 키워드
def profile(name, age, main_lang):
    print(name, age, main_lang)
#     순서 바뀌어도 호출 가능
profile(name="유재석",main_lang="python",age =20)
profile(main_lang="python",age =20, name="김태호")

# 가변인자 호출
def profile(name, age, main_lang1, lang2, lang3,lang4,lang5):
    print("이름: {0}\t나이: {1}\t".format(name,age),end =" ")
    print(main_lang1,lang2,lang3)

def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name,age),end =" ")
    for lang in language:
        print(lang, end=" ")
    print()

# 지역 변수와 전역변수

gun = 10

def checkpoint(soldiers):  #경계 근무
    # gun = 20
    global gun   # gun = 10
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2)      # 2명이 경계 근무
print("남은 총: {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
gun = checkpoint_ret(gun,2)
print("남은 총: {0}".format(gun))
