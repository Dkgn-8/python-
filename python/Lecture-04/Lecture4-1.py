#특수 메소드
'''
#은행 계좌 Solution , 2차원 벡터
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        return Vector2D(self.x + other.x , self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x , self.y - other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return '(%g, %g)' % (self.x,self.y)
    
u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
print(a)
'''


#선을 객체로 활용하기
class Line:
    def __init__(self, length):
        self.length = length
        print(self.length, '길이의 선이 생성되었습니다.')
    
    def __del__(self):
        print(self.length, '길이의 선이 제거되었습니다.')
    def __add__(self, other):
        return self.length + other.length
    def __lt__(self,other):
        return self.length < other.length
    def __eq__(self, other):
        return self.length == other.length

line1 = Line(10)
line2 = Line(5)
print('두 선의 합 : ',line1 + line2)

if line1 < line2:
    print('선2가 더 깁니다.')
elif line1 == line2:
    print('두 선의 길이가 같습니다.')
else:
    print('선 1이 더 깁니다.')
    del(line1)