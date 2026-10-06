#5-1
d = {"a":1,"a":9,"b":2}  #중복 키는 마지막값 적용
print(d["a"])
print(list(d.values()))
print("a" in d)

#5-2
d={"x":10}
print(d.get("y")) #None
print(d.get("y",0)) #키가 없으면 None 반환, 두 번째 인자를 주면 그 값을 반환
#print(d["y"]) #KeyError

#5-3
A = {1,2,3}
B = {3,4}
print(A&B) #교집합
print(A|B) #합집합
print(A-B) #차집합

#5-4 직접 작성
score = {"민수":80,"영희":95}
for a,b in score.items():
    print(a,":",b)