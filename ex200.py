#각 거래일의 수익금 : 시가(day_price[0]) - 종가(day_price[3]) ==>리스트에서 첫번째 숫자는 0번 ex)[1,2,3] 숫자1은 0번
#for문을 통해 total_profit의 값을 누적시켜 총 수익금의 값을 구하면 됨

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
        
total_profit = 0   #0에서부터 계속 for문을 돌며 수익금을 누적해감

for day_price in ohlc[1:]:    #크게 묶여있는 리스트 안의 첫번째 리스트는 수익금에 포함이 안되는 0번이므로 1번부터 for문을 돌림
    profit = day_price[0] - day_price[3]
    total_profit += profit    #total_profit = profit + total_profit
    
print(total_profit)    