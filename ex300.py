#파이썬 예외처리
#try:
#    실행 코드
#except:
#    예외가 발생했을 때 수행할 코드
#else:
#    예외가 발생하지 않았을 때 수행할 코드
#finally:
#    예외 발생 여부와 상관없이 항상 수행할 코드

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
   
#10.31
#==> float이므로 실행코드인 10.31이 먼저 출력되고 예외가 발생하지 않았으므로 clean data가 출력되고 finally에서의 변환 완료가 출력된다.
#""
#==> float이 아니므로 실행코드인 ""이 출력되지 않고 예외가 발생하였으므로 0이 출력되고 변환 완료가 출력된다.  
#8.00
#==> float이므로 실행코드인 8.00이 먼저 출력되고 예외가 발생하지 않았으므로 clean data가 출력되고 변환 완료가 출력된다.