#비교할 세 숫자를 a, b, c로 놓는다.
#def는 함수를 정의할 때 사용
def print_max(a, b, c):     #print_max()를 정의해준다.
    if a > b and a > c:     #a가 b보다 크고, a가 c보다 크다면 a가 가장 큰 수
        print(a)
    elif b > a and b > c:   #b가 a보다 크고, b가 c보다 크다면 b가 가장 큰 수
        print(b)
    else:                   #if문과 elif문이 모두 아니라면 else에서 print(c)
        print(c)
        
#위의 식이 잘 맞는지 확인하기 위하여 예시로 숫자를 비교해보면
print_max(17, 5, 8)                   #값 = 17 (if문을 만족하므로 a인 17이 도출)
print_max(17, 56, 8)                  #값 = 56 (if문을 만족시키지 못하고 elif문을 만족하므로 56이 도출)
print_max(17, 5, 85)                  #값 = 85 (if문과 elif문을 모두 만족시키지 못하므로 else문에 의해 85가 도출)
        
