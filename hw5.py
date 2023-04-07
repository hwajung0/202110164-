def read_single_digit(sd):
    if sd==1:
        return '일'
    elif sd==2:
        return '이'
    elif sd==3:
        return '삼'
    elif sd==4:
        return '사'
    elif sd==5:
        return '오'
    elif sd==6:
        return '육'
    elif sd==7:
        return '칠'
    elif sd==8:
        return '팔'
    else :
        return '구'
def read_number(num):
    num1=int(str(n)[0])
    num2=int(str(n)[1])
    num3=int(str(n)[2])
    n1=read_single_digit(num1)
    n2=read_single_digit(num2)
    n3=read_single_digit(num3)
    print(f'{n1} {n2} {n3}')

n=int(input('세 자리 정수 입력:'))
read_number(n)
