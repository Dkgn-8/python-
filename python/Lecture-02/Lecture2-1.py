'''
#클래스 작성하기
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1

a = Counter()
a.increment()
print("카운터의 값=",a.count)
'''

'''
#생성자
class Counter:
    def __init__(self, initValue = 0):
        self.count = initValue
    def increment(self):
        self.count += 1

a = Counter(100) #카운터의 초기값은 100이 된다.
b = Counter()    #카운터의 초기값은 0이 된다.
print("a의 카운터 값=%d , b의 카운터 값=%d" %(a.count,b.count))
'''

'''
#TV 클래스 정의 Solution
class Television:
    def __init__(self,channel,volune,on):
        self.channel = channel
        self.volume = volune
        self.on = on

    def show(self):
            print(self.channel, self.volume, self.on)

    def setChannel(self, channel):
            self.channel = channel

    def getChannel(self):
            return self.channel

t = Television(9,10,True)
t.show()

t.setChannel(11)
t.show()
'''
