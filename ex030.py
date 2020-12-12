#string 즉 문자열은 변경할 수 없는 자료형이기 때문에 replace를 하더라도 abcd가 그대로 출력된다.
#print(string)을 했을 경우 처음 입력해놓았던 string이 출력되기 때문이다. 
#string = 'abcd' //print를 제외한 string.replace('b' , 'B') 만을 입력해야 'aBcd'로 출력된다.
string = 'abcd'
string.replace('b' , 'B')
print(string)