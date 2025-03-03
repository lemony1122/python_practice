import sys

# data = sys.stdin.read().strip().split("\n")  # 전체 입력을 한 번에 읽고 줄 단위로 나눔
# n = int(data[0])  # 첫 줄에서 n 가져오기
#
# for i in range(1, n + 1):
#     a, b = map(int, data[i].split())
#     print(f"Case #{i}: {a}+{b} = {a+b}")  # f-string 사용


# data = sys.stdin.read().strip().split("\n")  # 전체 입력을 한 번에 읽고 줄 단위로 나눔
# n = int(data[0])  # 첫 줄에서 n 가져오기
#
# for i in range(1,n+1):
#     a = int(data[i][0])
#     average = sum(int(data[i]))
#
# import sys
#
# n = int(sys.stdin.readline())
# for _ in range(n):
#     arr =[]
#     a,b = map(int,sys.stdin.readline().strip().split(" "))
#     while True:
#         i = a % 10
#         if i not in arr:
#             arr.append(i)
#             a*=a
#         else:
#             l = len(arr)
#             b %= l
#             print(arr[b])
#             break


# total = int(sys.stdin.readline())
# n = int(sys.stdin.readline())
#
# temp = 0
# for _ in range(n):
#     a,b = map(int, sys.stdin.readline().split(" "))
#     temp += a*b
#
# print("True" if temp == total else "False")

# s = str(input())
# arr = [-1] * 26
# for idx, char in enumerate(s):
#     t = ord(char) - 97
#     if arr[t] == -1:
#         arr[t] = idx
#
# print(" ".join(map(str,arr)))

from queue import PriorityQueue

q = PriorityQueue()
for line in sys.stdin.read().splitlines():
     q.put(int(line))
while not q.empty():
    print(q.get())






