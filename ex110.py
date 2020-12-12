#이 코드는 크게 if와 else, 그리고 print("5")으로 구분되어 있다.
#맨 처음에 'True이면'이라고 하였으므로 else로 넘어가지 않고 if True에 계속 머무르게 된다.
#if True는 다시 if False와 else로 구분되어 있다. 그러므로 if False는 거짓이기때문에 넘어가게 되고 else의 값이 출력된다.
#따라서 위에서부터 아래로 내려와 출력되므로 if안의 else에서 print("3")이 출력되고 print("5") 또한 같이 출력되므로
#결과적으로 3과 5가 출력된다.


if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")