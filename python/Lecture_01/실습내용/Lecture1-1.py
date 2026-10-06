#format 활용
a = 1
b = 2

c = "{}더하기 {}은 {}입니다.".format(a,b,a+b)
print(c)


#if,else문 활용
#a = int(input("a: "))
a = 100
if a < 100:
    print("a가 100보다 작군요.")
elif a == 100:
    print("a는 100이군요.")
else:
    print("a가 100보다 크군요.")
    

#반복문 활용
for i in range(0,3,1):
    print("안녕하세요? for 문을 공부 중입니다. ^^!")
for i in [0,1,2]:
    print("안녕하세요? for 문을 공부 중입니다. ^^!")

b = 0
while True:
    print(123)
    b += 1
    if b == 10:
        break
    
    
#함수
def plus(v1,v2):
    result= 0
    result = v1 + v2
    return result

hap = 0
hap = plus(100,200)
print("100과 200의 plus()함수 결과는 %d" % hap)

#지역 변수와 전역 변수
def func1():
    a = 10
    print("func1()에서 a 값 %d" % a)
    
def func2():
    print("func2()에서 a 값 %d" % a)

#전역변수
a = 20

func1()
func2()


#global 예약어
def func1():
    global a
    a = 10
    print("func1()에서 a 값 %d" % a)
    
def func2():
    print("func2()에서 a값 %d" % a)

#함수 변수 선언 부분
a = 20 # 전역 변수

func1()
func2()


#변환 값이 여러 개인 함수
def multi(v1,v2):
    retList = [] #변환활 리스트
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList = []
hap, sub = 0, 0

myList = multi(100,200)
hap = myList[0]
sub = myList[1]
print("multi()에서 반환한 값 => %d %d" % (hap, sub))