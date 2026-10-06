#8-1
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

obj.__age는 class 은닉(private)으로 선언되어 있어 외부에서 접근할 수 없기 때문에 오류가 발생한다.
obj.getAge()를 통해 접근해야 한다.
'''

#8-2
class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def withdraw(self,amount):
        self.__balance -= amount
        print("통장에",amount,"가 출금되었음")
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
        print("통장에서",amount,"가 입금되었음")
        return self.__balance
    def getBalance(self):
        print("통장의 잔액은",self.__balance,"입니다.")
        return self.__balance

a = BankAccount()
a.deposit(70)
a.withdraw(20)
a.withdraw(80)
#70 50 -30

#8-3
# self.__balance

#8-4 직접작성
class Student:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.__age=age
        
    def getAge(self):  #접근자
        return self.__age
    def getName(self):
        return self.__name  
    def setAge(self,age):  #설정자
        if age >= 0:
            self.__age=age
    def setName(self,name):
        self.__name=name
