#9-1
a = [1,2]
b = a
c=[1,2]
b.append(3)
print(a) # [1,2,3] a와 b는 같은 리스트를 참조
print(c) # [1,2] c는 다른 리스트를 참조
print(a is b) # True
print(a == c) # False

#9-2
def f(t):
    t = None
    return t
myTV = [1213, 1234]
f(myTV)
print(myTV) # [1213, 1234] 함수 안에서 t에 None을 대입했지만, myTV는 영향을 받지 않는다. t는 myTV가 참조하는 리스트를 가리키고 있었지만, t = None으로 바뀌면서 더 이상 myTV를 참조하지 않게 되었다.

#9-3
class Television:
    seriaNumber = 0  #이것이 클래스 변수이다
    
    def __init__(self,channel,volume,on):
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.seriaNumber += 1  #클래스 변수를 하나 증가한다
        #클래스 변수의 값을 객체의 시리얼 번호로 한다.
        self.number = Television.seriaNumber
        
    def show(self):
        print(self.channel,self.volume,self.on,self.number)

a = Television(11,10,True)
b = Television(12,20,False)
s = a  #s는 a가 참조하는 객체를 참조한다. a와 s는 같은 객체를 참조한다.
#클래스카운터 = 2  (그러므로 클래스 카운터는 a,b 두개)
print(a.number) # 1
print(b.number) # 2

#9-4
#class Dog: kind="Bulldog" 이후 a=Dog(); b=Dog(); a.kind="Poodle"을 실행하면 a.kind, b.kind, Dog.kind는?
class Dog:
    kind = "Bulldog"
    def __init__(self,name,age):
        self.neme = name
        self.age = age
a = Dog("복실이",12)
b = Dog("깜돌이",2)
a.kind = "Podle"
print(a.kind)  #a에만 별도 인스턴스 속성이 생긴다.
print(b.kind)
print(Dog.kind)