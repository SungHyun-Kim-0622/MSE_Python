def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

#왼쪽:200, 오른쪽:100이 출력될 것이다.

#만약 my_print(100,200)이라고 썼다면 a에는 100이 들어가고 b에는 200이 들어가서 왼쪽:100, 오른쪽:200이 출력되겠지만
#a가 200이고 b가 100이라는 것을 명확하게 써준다면 순서가 바뀌더라도 b에는 100이 들어가고 a에는 200이 들어가게 되어 
#왼쪽:200, 오른쪽:100이 출력된다.