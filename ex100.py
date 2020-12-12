#zip이라는 함수는 key와 value를 묶어주는 역할을 한다. 여기서 date는 key, close_price는 value이므로 이 두개를 zip으로 묶고
#close_table 이름의 딕셔너리로 생성하기 위해서 zip 한 것을 dict에 넣어준 후 값을 출력한다.

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
