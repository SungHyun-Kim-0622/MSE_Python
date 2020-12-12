def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


#message3을 출력하라고 했으므로 def message3():으로 가고, for문을 3번 돌으라고 했으므로 
#message2()로 간 후 B를 출력 후 print("c")를 출력하는 것을 3번(i=0~i=2)반복한다.
#i는 0일 때  message2() ==> B
#          print("c") ==> C
#i는 1일 때  message2() ==> B
#          print("c") ==> C
#i는 2일 때  message2() ==> B
#          print("c") ==> C
#3번을 다 돈 후 message1을 출력하라고 하였으므로 message1()로 가서 출력한 후 끝 ==>A
#따라서 최종적인 답은 B,C,B,C,B,C,A(실제로는 한문자씩 세로줄로 값이 나옴)
