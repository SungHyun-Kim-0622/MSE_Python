#초기값(result)을 0으로 설정하면 계속 곱해도 0이 나오기 때문에 초기값을 1로 설정해준다.
#for문을 이용하여 반복적인 수행을 할 수 있도록 한다.

result = 1
for i in range(1,11):
    result = result * i
print(result)    

#i변수에 리스트의 숫자가 1부터 10(11-1)까지 차례대로 대입되어 result=1과 곱해진 후, 그 값이 다시 result에 대입되고
#다시 곱해진 result값과 다음 i값인 2와 곱해지면서 계속 이러한 과정을 반복하여 10까지의 숫자가 모두 곱해지게 된다.
# 1 * 1 = 2
# 2 * 2 = 4
# 4 * 3 = 12 .........                          