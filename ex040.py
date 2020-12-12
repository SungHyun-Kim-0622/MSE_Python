#문자열에서 strip을 이용하면 양쪽 끝에 있는 공백을 없앨 수 있다.(중간에 있는 공백은 제거할 수 없음) 
#data를 strip을 이용하여 data1을 새롭게 만들어 print한다면 공백이 제거된다 
data = "   삼성전자    "
data1 = data.strip()
print(data1)