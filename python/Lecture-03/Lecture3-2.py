'''
#은행 계좌 Solution
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
    
a = BankAccount()
a.deposit(100)
a.withdraw(10)
'''

'''
#객체를 함수로 전달할 떄
#텔레비전을 클래스로 정의한다.
class Television:
    def __init__(self,channel,volume,on):
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def show(self):
        print(self.channel,self.volume,self.on)
        
#전달받은 텔레비전의 음량을 줄인다.
def setSilentMode(t):
    t.volume = 2
    
#setSilentMode()을 호출하여 객체의 내용이 변경되었는지를 확인한다.
myTV = Television(11,10,True)
setSilentMode(myTV)
myTV.show()
'''

'''
#클래스 변수
#텔레비전을 클래스로 정의한다.
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
            
myTV = Television(11,10,True)
myTV.show()
'''

