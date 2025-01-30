# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
print(cabinet.get(5))    #cabinet[5] : 에러 터지고 하위 실행 안됨(프로그램 종료)    cabinet.get(5) : 에러 안 터지고 none 출력 후 다음 프로그램(hi) 실행
print(cabinet.get(5,"사용 가능"))
print("hi")

print(3 in cabinet)    # 존재 여부 확인 : True
print(10 in cabinet)   # False

# 값 추가
cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
cabinet2["C-20"] = "조세호"  #추가하는것
cabinet2["A-3"] = "김종국"  #덮어 쓰기

# 값 삭제
del cabinet2["A-3"]

# key 값 출력
print(cabinet2.keys())

# values 출력
print(cabinet2.values())

# key-value 값 출력
print(cabinet2.items())

# 전체 삭제
print(cabinet2.clear())
