# 리스트 []
#
# subway12 =10
# subway22=20
# subway32=30
# subway =[10,20,30]
from traceback import print_tb

# 조세호는 몇번째에 타고 있는가?
subway1 = ["유재석","조세호","박명수"]
print(subway1.index("조세호"))

# 하하가 다음 정류장에서 탐
subway1.append("하하")

# 정형동이 유재석, 조세호 사이에 탐
subway1.insert(1,"정형돈")  #인덱스에는 어디에 넣을건지

#뒤에서 꺼냄
print(subway1.pop())
print(subway1)

print(subway1.pop())
print(subway1)

print(subway1.pop())
print(subway1)

# 같은 이름의 사람이 몇명 있는지
subway1.append("유재석")
print(subway1)
print(subway1.count("유재석"))

# 정렬도 가능
num_list = [4,3,2,6,1]
num_list.sort()
print(num_list)

# 뒤짚기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()

# 다양한 자료형 함께 사용
mix_list = ["조세호",20,True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)