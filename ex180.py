#low_prices, high_prices 이 두개의 리스트의 5일간의 변동폭을 volatility의 리스트에 저장해야하므로
#for i in range()를 이용하고 append라는 함수를 사용하여 volatility 리스트에 저장한다.
#range 안에 들어갈 수는 low_prices의 개수(len(low_prices))로 
#리스트 안의 숫자 중 앞에서부터 0번~4번으로 총 5개가 존재하므로 5를 집어넣어서 for문을 돌아가게 한다.
#append는 원소를 마지막에 추가하거나 리스트에 자료를 추가할 때 사용한다. 

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [ ]
for i in range(5):
    변동폭 = high_prices[i] - low_prices[i]   
    volatility.append(변동폭)
    
print(volatility)    
