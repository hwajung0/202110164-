def get_radius(prompt):
    r= int(input(prompt))
    return r

print('넓이를 구하고자 하는 원의 반지름은?')
result=get_radius(prompt)
print('반지름',result,'인 원의 넓이=3.14*',result,'*',result)

def get_circle_area(radius):
    area=3.14*radius*radius
    return area
