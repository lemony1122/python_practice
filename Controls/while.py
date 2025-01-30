from http.cookiejar import cut_port_re

customer = "Jess"
index = 5

while index>=1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다." .format(customer,index))
    index-=1
    if index==0:
        print("커피는 폐기처분 되었습니다")


# 무한루프
# buyer = "아이언맨"
# count =1
# while True:
#     print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다." .format(buyer,count))
#     count +=1

customer1 = "토르"
person = "un"
while person!=customer1:
    print("{0}, 커피가 준비되었습니다.".format(customer1))
    person =  input("이름이 어떻게 되세요?")

