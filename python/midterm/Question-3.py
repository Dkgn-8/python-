#3-1 출력예측
def f(x):
    sum = 0
    sum = print(x+1)
    return sum
a = f(2)

#3-2
x = 5
def f():
    x = 9
    return x
print(x) #5

#3-3
def sub(x,y,z=0):
    return x-y-z
print(sub(10,y=3))
print(sub(z=2,y=3,x=10))
#일반 호출에서는 위치 인수를 먼저, 키워드 인수를 뒤에 둔다. f(x=10, 20)은 SyntaxError. 같은 매개변수에 값을 중복 전달하면 TypeError.

#3-4 직접 작성
def multi(x,y):
    return [x+y,x-y]
a,b = multi(8,3)
print(a)
print(b)