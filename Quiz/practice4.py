import random
from random import randrange

# values = random.sample(range(5,51),k=50)
# waiting = {id: value for id, value in zip(range(1,51),values)}
# print(waiting)


cnt = 0 #총 탑승객 수
for i in range(1,51) :
    time = randrange(5,51) #5~51분 소요시간
    if 5<=time <=15:
        print("[O] {0}번째 손님 (소요시간 :{1}분)".format(i,time))
        cnt+=1
    else: #매칭 실패한 경우
        print("[ ] {0}번쨰 손님 (소요시간: {1}분)".format(i,time))
print("총 탑승객: {0}분".format(cnt))
