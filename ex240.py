def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

#28의 결과값이 나올 것이다.

#return은 값을 반환하기(돌려주기) 위해 사용한다.
#c=함수2에 2를 넣은 값인데 print(c)를 하였으므로 
#def 함수2(num): 에서 num자리에 2를 넣으면 다시 num은 2 + 10 = 12 
#==> 이 값(12)을 다시 함수1(num)으로 가서 return 시키므로
#def 함수1(num): 에서 num자리에 12를 넣으면 12 + 2 = 14 
#==> 이 값(14)를 다시 함수0으로 return 시키면 return 14 * 2 = 28이므로
#함수0에서 return되고 함수1에서 return되고 함수2에서 return되어 
#최종적으로 print(c)를 하면 28의 결과값이 나온다.