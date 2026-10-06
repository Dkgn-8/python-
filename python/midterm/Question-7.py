#7-1
class Counter:
    def __init__(self, initValue=0):
        self.count = initValue
    def increment(self):
        self.count += 1
a = Counter(3)
b = Counter()
a.increment()
b.increment()
print(a.count)  #4
print(b.count)  #1

#7-2 오류수정
'''
class Counter:
    def __init__(self, initValue=0):
        self.count = initValue
    def increment(self):
        count += 1  #self.count로 수정
'''

#7-3
'''
클래스: 객체를 만들기 위한 설계도
인스턴스: 클래스로부터 만들어진 객체
'''

#7-4 직접작성
class Television:
    def __init__(self, channel=9):
        self.channel = channel
    def setChannel(self, channel):
        self.channel = channel
    def getChannel(self):   
        return self.channel
    def show(self):
        print("Channel:", self.channel)
a = Television()
a.show()
a.setChannel(11)
a.show()    