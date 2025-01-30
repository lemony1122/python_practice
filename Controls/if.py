weather = "눈"

if weather == "비" or "눈":   #if weather == "비" or weather =="눈"
    print("우산을 챙기세요")
elif weather == "미세먼저":
    print("마스크를 챙기세요")
else :
    print("날씨가 좋습니다😊")


temp = int(input("기온이 어떄요?"))
if temp >=30 :
    print("날씨가 너무 더워요")
elif 10 <= temp <30 :   # 10<=temp and temp<30
    print("😊😊")
else :
    print("너무 추워요 나가지 마세요")