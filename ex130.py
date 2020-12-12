#if를 사용하여 (시가 + 변동폭)>최고가일 경우 "상승장"이 출력되게 하고, 그렇지 않은 경우 else를 사용하여 "하락장" 이 출력되게 한다.
#변동폭은 최고가(max_price)에서 최저가(min_price)를 뺀 값이고 시가는 opening_price로 둔다. (#btc => 비트코인)
#또한 float를 이용하여 실수형으로 만들어준다. import는 다른 프로그램으로부터 데이터를 갖고 오는 역할을 한다.(아래의 주소를 요청(request)함)
#여기서 'max_price', 'min_price', 'opening_price' 는 모두 딕셔너리의 key에 해당된다.


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])   
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가 + 변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")