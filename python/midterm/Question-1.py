#1-1 출력 예측
print(7/2, 7//2, 7%2,2**3)  #3.5  3  1  8

#1-2 두 수의 합
a = input("Enter a number: ")
b = input("Enter a number: ")
print(int(a) + int(b))

#1-3 오류 수정
#print("%d %d" , %10)
print("%d %d" % (10, 20))

#1-4 두 수의 합과 나머지
a= int(input('정수를 입력하시오: '))
b= int(input('정수를 입력하시오: '))
print('합:', a + b)
print('나머지:', a % b)