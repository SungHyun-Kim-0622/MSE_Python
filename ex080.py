#1부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하기 위해서는 tuple(range(시작숫자, 마지막숫자+1, 얼만큼씩 증가하는지))를 사용한다. 
#짝수인 2부터 시작하여 (99+1)까지의 범위를 설정하고 2씩 증가하게 숫자를 출력하면 된다.

data = tuple(range(2,100,2))
print(data)