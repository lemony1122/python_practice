#open: 파일 열기, w: 쓰기 utf8: 한글(항상 쓰는걸 추천)
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file =score_file)
# print("영어 : 50", file =score_file)
# score_file.close()

# 만약 그대로 w을 쓰면 덮어쓰기 --> 이미 존재하는 파일에 내용 추가  -> a(append)
score_file = open("score.txt", "a", encoding="utf8")
# write는 자동 줄 바꿈 안됨
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()


#r: 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())  #파일의 모든 내용 읽기
score_file.close()

#
score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline())
print(score_file.readline())
#줄 바꿈 안함 (print는 자동 줄바꿈)
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

# 줄이 얼마나 있는지 모를때
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
    # print(line,end="")
score_file.close()

#list에 다 넣어버림
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()  # 리스트 형태로 저장
for line in lines:
    print(line,end="")
score_file.close()

