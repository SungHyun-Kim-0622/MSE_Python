#리스트에 있는 값을 오름차순으로 정리하는 방법은 두가지가 있다.
#첫번째 방법(data의 기존값을 바로 오름차순으로 정리함) 
#data = [2, 4, 3, 1, 5, 10, 9]
#data.sort()
#print(data)

#두번째 방법(기존의 data값은 그대로 두고 data1을 이용하여 새롭게 data를 정리함)
data = [2, 4, 3, 1, 5, 10, 9]
data1 = sorted(data)
print(data1)