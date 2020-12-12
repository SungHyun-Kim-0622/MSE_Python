#class를 omg라는 변수가 바인딩
#"."찍으면 class에 정의되어있는 함수를 불러옴


class OMG : 
    def print() :           #현재 print함수에는 인자가 없음    
        print("Oh my god")


myStock = OMG()
myStock.print()     #객체를 쓰고 "."을 찍으면 OMG.print(mystock)이라고 인식됨.  ==> 오류발생
#mystock이 추가적으로 인자로 넘어가게 됨. 따라서 def print() : 안에 아무것도 없기 때문에 오류가 발생하게 됨.
#기본적으로 괄호안에 "self"를 씀.


#고친 예(print하면 oh my god이 출력됨)
#class OMG : 
#    def print(self) :          
#        print("Oh my god")


#myStock = OMG()
#myStock.print()