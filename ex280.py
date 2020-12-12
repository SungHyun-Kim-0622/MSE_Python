import random


class Account:
    # class variable(class 공간안에 변수생성)
    account_count = 0   #account_count가 0을 바인딩함.

    def __init__(self, name, balance):        #예금주, 잔고
        self.deposit_count = 0      #입금한 횟수는 한번도 없으므로 0으로 초기화
        self.deposit_log = []       
        self.withdraw_log = []

        self.name = name                     #self가 가리키는 공간에 name을 바인딩함.
        self.balance = balance
        self.bank = "SC은행"                   #은행이름

        # 3-2-6 (계좌번호)
        num1 = random.randint(0, 999)     #3자리 숫자를 랜덤하게 나오도록 설정
        num2 = random.randint(0, 99)      #2자리 숫자를 랜덤하게 나오도록 설정
        num3 = random.randint(0, 999999)  #6자리 숫자를 랜덤하게 나오도록 설정

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'     ==> 정수값을 문자열로 바꿔줌
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001 
        Account.account_count += 1    #계좌가 증가될 때마다 0부터 1씩 증가

    @classmethod   #객체에 접근할 필요가 없을 때 사용.
    def get_account_num(cls):     
        print(cls.account_count)  # = Account.account_count

    def deposit(self, amount):        #잔고에 접근하기 위하여 self로 받아야함.
        if amount >= 1:               #1원 이상이여야함.
            self.deposit_log.append(amount)   #입금내역을 deposit_log에 리스트로 저장
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5로 나누었을 때 0으로 떨어지면(5의 배수)
                                                    # 이때 이자 지급
                self.balance = (self.balance * 1.01)  #1%의 이자를 지급


    def withdraw(self, amount):      #출금 method , 얼마를 출금할껀지 amount로 받음
        if self.balance > amount:    # 잔고가 출금요청액 이상일 때만 가능(출금요청액이 더 많으면 마이너스가 되는데 그러한 경우는 거의 없음.) 
            self.withdraw_log.append(amount)  #출금내역을 withdraw_log에 리스트로 저장
            self.balance -= amount        #잔고 - 출금요청액

    def display_info(self):           #은행이름, 예금주, 계좌번호, 잔고를 self로 가져옴
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):     #출금내역
        for amount in self.withdraw_log:    
            print(amount)

    def deposit_history(self):      #입금내역
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)    #처음에 1000원을 넣음
k.deposit(100)
k.deposit(200)
k.deposit(300)   #100원, 200원, 300원을 입금.
k.deposit_history()  

k.withdraw(100)
k.withdraw(200)   #100원, 200원 출금
k.withdraw_history()