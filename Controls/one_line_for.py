student = [1,2,3,4,5]
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
students = ["Iron","Thor","Groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students2= ["IronMan","Thor", "Teddy"]
students2 = [i.upper() for i in students2]
print(students2)