#기본 데이터형
boolVal = 100 > 200
print(boolVal)
print(type(boolVal))

intVal = 100 ** 100
print(intVal)
print(type(intVal))


#리스트
aa = [10,20,30,40]
print(aa[0])
aa[1] = 200
print(aa)
aa.append(0)
print(aa)

aa = []
for i in range(0,100):
    aa.append(0)
print(len(aa))


aa = []
for i in range(0,4):
    aa.append(0)
hap = 0
for i in range(0,4):
    aa[i] = int(input(str(i + 1) + "번째 숫자: "))
for i in range(0,4):
    hap = hap +aa[i]
print("합계 = %d" % hap)


#2차원 리스트
aa = [[111],[222],[333],
      [444],[555],[666],
      [777],[888],[999]]

list1=[]
list2=[]
value =1
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 =[]
for i in range(0,3):
    for k in range(0,4):
        print("%3d" % list2[i][k], end =' ')
    print(" ")
    
    
#리스트 = [수식 for 항목 in range() if 조건식]
numlist = [num*num for num in range(1,6)]
print(numlist) #[1,4,9,16,25]

#2차원 리스트 = [[수식 for 항목 in rnage()] for 항목 in range()]
list2 = [[0 for _ in range(4)] for _ in range(3)]
print(list2) #[[0,0,0,0],[0,0,0,0],[0,0,0,0]]


#딕셔너리 = [키1:값1, 키2:값2, 키3:값3]
student1 = {'학번':2600025, '이름':'김도경', '학과':'컴퓨터학과'}
student1['연락처'] = '010-1111-2222' 
print(student1) #{'학번':2600025, '이름':'김도경', '학과':'컴퓨터학과', '연락처':'010-1111-2222'}
student1['학과'] = '파이썬학과'
print(student1) #{'학번':2600025, '이름':'김도경', '학과':'파이썬학과', '연락처':'010-1111-2222'}

del(student1['학과'])
print(student1) #{'학번':2600025, '이름':'김도경', '연락처':'010-1111-2222'}

student1 = {'학번':2600025, '이름':'김도경', '학과':'컴퓨터학과', '학번': 2000}
print(student1) #{'학번':2000, '이름':'김도경', '학과':'컴퓨터학과'}
#     *동일한 키를 갖는 딕셔너리는 마지막 키가 적용됨*

print(student1['학번']) #2000     #딕셔너리[키]는 없는 키를 호출하면 오류 발생
print(student1.get('이름')) #김도경     #.get은 키가 없다면 아무것도 호출하지 않음 오류X

print(student1.keys()) #dict_keys(['학번','이름','학과'])
print(student1.values()) #dict_value(['2000','김도경','파이썬학과'])
#       list(딕셔너리이름.keys() or  value())시 dict_ 없앨 수 있음
student1.items() #dict_items([('학번', 2000), ('이름', '김도경'), ('학과', '파이썬학과')])
#      딕셔너리이름.items() 함수를 사용하면 튜프 형태도 구할 수 있음

print('이름' in student1) #True
print('주소' in student1) #False

sigger = {'이름': '트와이스', '구성원 수': 9, '데뷔': '서바이벌 식스틴', '대표곡': 'SIGNAL'}
for k in sigger.keys():
    print('%s --> %s' % (k, sigger[k]))
'''
이름 --> 트와이스
구성원 수 --> 9
데뷔 --> 서바이벌 식스틴
대표곡 --> SIGNAL
'''


#세트 = {'키1','키2','키2','키3','키3','키3','키4'} --> {키1,키2,키3,키4}
mySet1 = {1,2,3,4,5}
mySet2 = {4,5,6,7}


#문자열
ss = "자료구조&알고리즘"
print(ss[0])  # '자'
print(ss[1:4])  # '료구조' 
print(ss[4:])  # '&알고리즘'

ss = '파이썬' + '최고' # '파이썬최고'
ss = '파이썬' * 3 # '파이썬파이썬파이썬'
ss = '파이썬abcd'
print(len(ss)) # 7

ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠.^^'
print(ss.count('공부'))  #찾을문자열의 개수
print(ss.find('공부'))  #찾을문자열이 왼쪽부터 몇 번째에 위치하는지    #찾을 문자열이 없으면 -1을 반환
print(ss.rfind('공부'))  #find()와 반대로 오른쪽부터 찾음
print(ss.index('공부'))  #find()와 동일하지만 찾을 문자열이 없다면 오류 발생

ss = 'Python을 열심히 공부 중'
print(ss.split()) #['Python을', '열심히', '공부', '중']
 
 
#함수 이름 대입
before = ['2022','12','31']  
after = list(map(int, before)) #map함수는 리스트의 문자열 하나하나를 함수 이름에 대입
print(after) #[2022, 12, 31]


#튜플
tt1 = (10, 20, 30)
tt2 = 10, 20, 30   #튜플은 ()를 생략해도 됨
tt3 = (10)
tt4 = 10   #tt3, tt4는 튜플이 아님
tt5 = (10,)
tt6 = 10,  #항목이 하나인 튜플은 뒤에 쉼표(,)를 붙여야 함

'''
tt1.append(40)
tt1[0] = 40
del(tt1[0])
   *튜플은 읽기 전용이므로 다음 코드는 오류 발생*

del(tt1)
del(tt2)
   *튜플 자체를 del()함수로 삭제 할 수 있음
'''

myTuple = (10,20,30)
myList = list(myTuple)  
myList.append(40)
myTuple = tuple(myList)  #튜플 -> 리스트 -> 튜플로 변환한 예
print(myTuple) #(10,20,30,40)

