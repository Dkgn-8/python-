'''
class Car:
    def __init__(self,speed,color,model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

myCar = Car(0,"blue","E-class")

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는",myCar.speed)
print("자동차의 색상은",myCar.color)
print("자동차의 모델은",myCar.model)

myCar.drive()
print("자동차의 속도는",myCar.speed)
'''


#정보은닉(private) : 변수 이름 앞에 __을 붙이면 된다.
#private이 붙은 인스턴스 변수는 클래스 내부에서만 접글될 수 있다.

'''
class Student:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.__age=age
        
    def getAge(self):  #접근자
        return self.__age
    def getName(self):
        return self.__name  
    def setAge(self,age):  #설정자
        self.__age=age
    def setName(self,name):
        self.__name=name
        
obj=Student("Hong",20)
print(obj.getName())
'''