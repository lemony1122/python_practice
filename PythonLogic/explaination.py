# 함수
# def 함수명(변수1, 변수2....):
#     print("새로운 계좌가 생성되었습니다.")

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다. ".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance>=money:
        balance-=money
        print("출금이 완료되엇습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
    else:
        print("오류")
        return balance

balance = 0
balance = deposit(balance,1000)
print(balance)
print(withdraw(balance,20))