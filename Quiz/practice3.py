from random import randint, shuffle, sample

list = list(range(1,20))
shuffle(list)
chicken = list.pop()
coffee = sample(list,3)


announcement = f"""
--- 당첨자 발표 ---
치킨 당첨자 : {chicken}
커피 당첨자 : {coffee}
--- 축하합니다 ---
"""

print(announcement)
#
# lst = list(range(1,20))
# shuffle(lst)
# print(lst)
# print(sample(lst,2))