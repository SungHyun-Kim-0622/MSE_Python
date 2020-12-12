class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):    # name, code, per, pbr, 배당수익률 값을 가져옴.
        self.name = name     #self라는 공간안에 name이 가리키는 문자열타입의 객체 name을 바인딩하라는 뜻 ==> 생성자를 정의
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):   #self가 가리키는 코드를 새로받은 name으로 setting하라는 뜻 
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):            #어느 객체에서 가져올껀지 setting해줌.(종목명과 종목코드를 return함.)
        return self.name

    def get_code(self):
        return self.code 
   
    def set_per(self, per):         #per, pbr, 배당수익률은 변경될 수 있는 값이기 때문에 
        self.per = per              #self가 가리키는 코드를 새로받은 per, pbr, 배당수익률로 setting

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_배당수익률(self, 배당수익률):
        self.배당수익률 = 배당수익률        



종목 = []   #'종목'이라는 리스트를 만듬
#stock class(삼성, 현대차, LG전자)   

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)   #stock class의 객체를 만듬
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)       #종목이라는 리스트 안에 삼성, 현대차, LG전자를 append함.
종목.append(현대차)
종목.append(LG전자)

for i in 종목:            #i는 삼성, 현대차, LG전자를 바인딩 함.
    print(i.code, i.per)    #i ==> stock class의 객체를 바인딩하기 때문에 "i.code, i.per"라고 쓸 수 있다.