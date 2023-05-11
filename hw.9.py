class Rectangle:
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def show(self):
        print(f'좌측 상단 꼭짓점이 ({self.x1},{self.y1})이고 우측 상단 꼭짓점이 ({self.x2},{self.y2})인 사각형 입니다.')

    def getWidth(self):
        return self.x2-self.x1

    def getHeight(self):
        return self.y2-self.y1
    
    def getArea(self):
        return (self.x2-self.x1)*(self.y2-self.y1)
    
    def getPerimeter(self):
        return (self.y2-self.y1)*2+(self.x2-self.x1)*2
    
# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')