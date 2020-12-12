#numpy는 수치 해석용 파이썬 패키지를 말한다.
#평소 for문에서 for i in range():를 사용하는데 이 경우 0.1같은 실수 단위는 사용하지 못하고 정수만 가능하다.
#하지만 for i in numpy.arange():는 실수 단위까지 사용할 수 있다.



import numpy
for i in numpy.arange(0, 5, 0.1):     #0.0부터 5.0까지 0.1씩 증가
    print(i)