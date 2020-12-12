#파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력해야하므로 or을 사용하여 나타낸다.
#split함수는 문자열을 공백 혹은 어떠한 기준으로 나눌 때 사용하는 함수로 여기서 사용할 때는 '.' 을 기준으로 
#파일의 이름(name)과 확장자(ext)를 구분(분리)한다.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    name, ext = i.split('.')
    if ext == 'h' or ext == 'c':      #확장자(ext)가 h거나 c라면,,
        print(i)