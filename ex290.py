class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):           #자식class는 부모 class를 상속받음
  def __init__(self):
    print("자식생성")
    super().__init__()    #self는 알아서 전달이 됨.(쓸 필요 X)

나 = 자식()

#자식생성이 먼저 출력되고, super().__init__()에 의해 "부모생성"이 출력됨.
#super. ==> 부모 class에 접근가능(부모 class를 명시적으로 호출가능)
