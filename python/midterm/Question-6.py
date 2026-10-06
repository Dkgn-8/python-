#6-1
s = "ababa"
print(s.count("a"))
print(s.find("ba"))
print(s.rfind("ba"))
print(s.find("c")) #찾는 문자열이 없으면 -1 반환

#6-2
s = ["10","20","30"]
s1 = list(map(int,s)) #map(함수,반복가능객체) : 반복가능객체의 각 원소에 함수를 적용한 결과를 map 객체로 반환
print(s1)

#6-3
a = (10)  #int형
b = (10,)  #튜플은 원소가 하나일 때 반드시 콤마를 붙여야 한다
#b[0] = 20  #튜플은 원소를 변경할 수 없다. TypeError

#6-4 직접 작성
c = ["Python","시험","공부"]
c1 = "/".join(c)  #리스트의 각 원소를 문자열로 연결하여 하나의 문자열로 반환
print(c1)